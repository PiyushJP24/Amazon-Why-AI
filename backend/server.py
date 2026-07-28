"""WhyAI backend — FastAPI + MongoDB + Gemini RAG."""
import os
import uuid
import logging
import asyncio
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, APIRouter, HTTPException
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from google.genai import errors as genai_errors

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")

from seed_products import PRODUCTS, all_products_summary, get_product, CLUSTERS  # noqa: E402
from seed_reviews import flatten_all_reviews  # noqa: E402
from gemini_client import embed_texts, embed_one, extract_use_case, generate_feature_cards, tell_me_more  # noqa: E402
from rag import retrieve_specs, review_confidence_per_feature  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("whyai")

# --- Mongo ---
mongo_url = os.environ["MONGO_URL"]
mongo_client = AsyncIOMotorClient(mongo_url)
db = mongo_client[os.environ["DB_NAME"]]

# --- App ---
app = FastAPI()
api = APIRouter(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- In-memory KBs (embeddings computed once on startup) ---
SPEC_KB: List[dict] = []   # [{id, product_id, feature_name, technical_meaning, benefit_templates, embedding}]
REVIEW_KB: List[dict] = [] # [{id, product_id, review_text, sentiment, inferred_use_case_cluster, embedding}]

# Response cache: (product_id, use_case_text.lower().strip()) -> generate response
_GEN_CACHE: dict = {}
_TELL_CACHE: dict = {}


# --- Models ---
class WhyAIRequest(BaseModel):
    use_case_text: str
    product_id: str
    session_id: Optional[str] = None


class TellMoreRequest(BaseModel):
    use_case_text: str
    cluster: str
    product_id: str
    feature_name: str


class FeedbackRequest(BaseModel):
    session_id: str
    product_id: str
    feature_name: str
    thumbs: str  # "up" or "down"


# --- Startup: build KBs + embeddings ---
@app.on_event("startup")
async def startup():
    logger.info("Building spec KB embeddings...")
    spec_entries_raw = []
    spec_texts = []
    for p in PRODUCTS:
        for f in p["features"]:
            # Embed a rich text: feature + technical meaning
            text = f"{f['feature_name']}. {f['technical_meaning']}"
            spec_texts.append(text)
            spec_entries_raw.append({
                "id": f"spec-{p['id']}-{f['feature_name']}",
                "product_id": p["id"],
                "feature_name": f["feature_name"],
                "technical_meaning": f["technical_meaning"],
                "benefit_templates": f["benefit_templates"],
                "_embed_text": text,
            })

    logger.info("Embedding %d spec entries...", len(spec_texts))
    spec_vecs = await asyncio.to_thread(embed_texts, spec_texts, "RETRIEVAL_DOCUMENT")
    for entry, vec in zip(spec_entries_raw, spec_vecs):
        entry["embedding"] = vec
        SPEC_KB.append(entry)

    logger.info("Building review KB embeddings...")
    reviews_raw = flatten_all_reviews()
    review_texts = [r["review_text"] for r in reviews_raw]
    logger.info("Embedding %d reviews...", len(review_texts))
    review_vecs = await asyncio.to_thread(embed_texts, review_texts, "RETRIEVAL_DOCUMENT")
    for r, v in zip(reviews_raw, review_vecs):
        r["embedding"] = v
        REVIEW_KB.append(r)

    logger.info("KBs ready. specs=%d reviews=%d", len(SPEC_KB), len(REVIEW_KB))


@app.on_event("shutdown")
async def shutdown():
    mongo_client.close()


# --- Routes ---
@api.get("/")
async def root():
    return {"ok": True, "app": "WhyAI", "kb_ready": len(SPEC_KB) > 0 and len(REVIEW_KB) > 0,
            "specs": len(SPEC_KB), "reviews": len(REVIEW_KB)}


@api.get("/products")
async def get_products():
    return {"products": all_products_summary()}


@api.get("/products/{product_id}")
async def get_product_detail(product_id: str):
    p = get_product(product_id)
    if not p:
        raise HTTPException(404, "Product not found")
    return p


@api.post("/whyai/generate")
async def whyai_generate(req: WhyAIRequest):
    if len(SPEC_KB) == 0 or len(REVIEW_KB) == 0:
        raise HTTPException(503, "Knowledge base still warming up. Try again in a few seconds.")
    product = get_product(req.product_id)
    if not product:
        raise HTTPException(404, "Product not found")

    # Response cache to preserve LLM quota on repeated demos of the same query
    cache_key = (req.product_id, req.use_case_text.strip().lower())
    cached = _GEN_CACHE.get(cache_key)
    if cached is not None:
        # Still log the session so feedback works
        session_id = req.session_id or str(uuid.uuid4())
        session_doc = {
            "id": session_id,
            "use_case_text": req.use_case_text,
            "use_case_cluster": cached["use_case"]["cluster"],
            "normalized_description": cached["use_case"]["normalized_description"],
            "product_id": req.product_id,
            "response_json": cached["cards"],
            "feedback": [],
            "cached": True,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        await db.sessions.insert_one(session_doc)
        return {"session_id": session_id, **cached}

    try:
        # 1) Extract use case (LLM)
        uc = await asyncio.to_thread(extract_use_case, req.use_case_text)
        cluster = uc["cluster"]

        # 2) Embed the use-case text once
        query_vec = await asyncio.to_thread(embed_one, req.use_case_text, "RETRIEVAL_QUERY")

        # 3) Retrieve specs (per-cluster benefit_template selected, includes embeddings)
        retrieved = retrieve_specs(req.product_id, cluster, query_vec, SPEC_KB)

        # 4) Per-feature use-case-matched review confidence (two-layer RAG)
        conf = review_confidence_per_feature(
            req.product_id, cluster, query_vec, REVIEW_KB, retrieved
        )

        # 5) Generate personalized cards (LLM) — strip embeddings before passing
        retrieved_for_gen = [{"feature_name": r["feature_name"],
                              "technical_meaning": r["technical_meaning"],
                              "benefit_template": r["benefit_template"]}
                             for r in retrieved]
        cards = await asyncio.to_thread(
            generate_feature_cards, req.use_case_text, cluster, product["name"], retrieved_for_gen, conf
        )
    except genai_errors.ClientError as e:
        status = getattr(e, "code", None) or getattr(e, "status_code", 500)
        if status == 429:
            raise HTTPException(429, "The AI service is rate-limited right now. Please try again in a minute.")
        logger.exception("Gemini client error: %s", e)
        raise HTTPException(503, "The AI service returned an error. Please try again.")
    except Exception as e:
        logger.exception("whyai_generate failed: %s", e)
        raise HTTPException(500, "Something went wrong generating your WhyAI insights.")

    # 6) Session logging
    session_id = req.session_id or str(uuid.uuid4())
    payload = {
        "use_case": {
            "raw": req.use_case_text,
            "cluster": cluster,
            "normalized_description": uc["normalized_description"],
        },
        "cards": cards,
    }
    _GEN_CACHE[cache_key] = payload

    session_doc = {
        "id": session_id,
        "use_case_text": req.use_case_text,
        "use_case_cluster": cluster,
        "normalized_description": uc["normalized_description"],
        "product_id": req.product_id,
        "response_json": cards,
        "feedback": [],
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    await db.sessions.insert_one(session_doc)

    return {"session_id": session_id, **payload}


@api.post("/whyai/tell-more")
async def whyai_tell_more(req: TellMoreRequest):
    product = get_product(req.product_id)
    if not product:
        raise HTTPException(404, "Product not found")

    # Find the feature spec
    feature = None
    for f in product["features"]:
        if f["feature_name"] == req.feature_name:
            feature = f
            break
    if not feature:
        raise HTTPException(404, "Feature not found")

    benefit_template = feature["benefit_templates"].get(req.cluster) \
        or next(iter(feature["benefit_templates"].values()))

    cache_key = (req.product_id, req.feature_name, req.cluster, req.use_case_text.strip().lower())
    cached = _TELL_CACHE.get(cache_key)
    if cached is not None:
        return {"explanation": cached}

    try:
        text = await asyncio.to_thread(
            tell_me_more,
            req.use_case_text, req.cluster, product["name"], req.feature_name,
            feature["technical_meaning"], benefit_template,
        )
    except genai_errors.ClientError as e:
        status = getattr(e, "code", None) or getattr(e, "status_code", 500)
        if status == 429:
            raise HTTPException(429, "The AI service is rate-limited right now. Please try again in a minute.")
        logger.exception("Gemini tell-more error: %s", e)
        raise HTTPException(503, "The AI service returned an error.")
    _TELL_CACHE[cache_key] = text
    return {"explanation": text}


@api.post("/whyai/feedback")
async def whyai_feedback(req: FeedbackRequest):
    if req.thumbs not in {"up", "down"}:
        raise HTTPException(400, "thumbs must be 'up' or 'down'")
    entry = {
        "product_id": req.product_id,
        "feature_name": req.feature_name,
        "thumbs": req.thumbs,
        "at": datetime.now(timezone.utc).isoformat(),
    }
    await db.sessions.update_one({"id": req.session_id}, {"$push": {"feedback": entry}})
    return {"ok": True}


@api.get("/whyai/health")
async def health():
    return {
        "kb_ready": len(SPEC_KB) > 0 and len(REVIEW_KB) > 0,
        "specs": len(SPEC_KB),
        "reviews": len(REVIEW_KB),
    }


app.include_router(api)

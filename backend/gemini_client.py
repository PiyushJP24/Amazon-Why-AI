"""Gemini client wrappers for WhyAI: text generation + embeddings with disk cache."""
import os
import json
import hashlib
import time
import logging
from pathlib import Path
from typing import List

from google import genai
from google.genai import types, errors as genai_errors

logger = logging.getLogger(__name__)

_client = None

CACHE_PATH = Path(__file__).parent / "data" / "embedding_cache.json"
_cache = None


def _load_cache():
    global _cache
    if _cache is None:
        if CACHE_PATH.exists():
            try:
                with open(CACHE_PATH, "r") as f:
                    _cache = json.load(f)
            except Exception:
                _cache = {}
        else:
            _cache = {}
    return _cache


def _save_cache():
    if _cache is None:
        return
    CACHE_PATH.parent.mkdir(exist_ok=True, parents=True)
    tmp = CACHE_PATH.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(_cache, f)
    tmp.replace(CACHE_PATH)


def _key(text: str, task_type: str) -> str:
    h = hashlib.sha256((task_type + "::" + text).encode("utf-8")).hexdigest()
    return h


def get_client():
    global _client
    if _client is None:
        api_key = os.environ["GEMINI_API_KEY"]
        _client = genai.Client(api_key=api_key)
    return _client


TEXT_MODEL = os.environ.get("TEXT_MODEL", "gemini-3.5-flash-lite")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "gemini-embedding-001")
EMBED_DIM = 768


def _generate_with_retry(**kwargs):
    """Wrap client.models.generate_content with retry on transient 503 UNAVAILABLE.
    Gemini's error message explicitly says these are 'usually temporary'."""
    client = get_client()
    # Primary: gemini-3.5-flash-lite (15 rpm / 500 rpd on free tier).
    # Fallback: gemini-3.5-flash (5 rpm / 20 rpd) — used only if the primary
    # is exhausted after retries.
    primary = kwargs.pop("model", TEXT_MODEL)
    fallbacks = [primary, "gemini-3.5-flash"]
    # De-dupe while preserving order
    seen = set()
    ordered = [m for m in fallbacks if not (m in seen or seen.add(m))]

    last_err = None
    for model in ordered:
        for attempt in range(3):
            try:
                return client.models.generate_content(model=model, **kwargs)
            except genai_errors.ServerError as e:
                code = getattr(e, "code", None) or getattr(e, "status_code", 500)
                if code == 503:
                    delay = 0.8 * (2 ** attempt)  # 0.8s, 1.6s, 3.2s
                    logger.warning("503 on %s (attempt %d), backing off %.1fs", model, attempt + 1, delay)
                    last_err = e
                    time.sleep(delay)
                    continue
                raise
            except genai_errors.ClientError:
                raise
        logger.warning("Model %s exhausted retries — trying next fallback", model)
    # All fallbacks exhausted
    raise last_err if last_err else RuntimeError("Gemini generate_content failed with no captured error")


def embed_texts(texts: List[str], task_type: str = "RETRIEVAL_DOCUMENT") -> List[List[float]]:
    """Embed a list of texts. Uses disk cache. Throttled to stay under free-tier
    rate limit (~100 items/minute)."""
    if not texts:
        return []
    cache = _load_cache()

    # Fast path: fully cached
    result: List[List[float]] = [None] * len(texts)  # type: ignore
    to_fetch_idx = []
    to_fetch_texts = []
    for i, t in enumerate(texts):
        k = _key(t, task_type)
        if k in cache:
            result[i] = cache[k]
        else:
            to_fetch_idx.append(i)
            to_fetch_texts.append(t)

    if not to_fetch_texts:
        return result

    client = get_client()
    B = 10  # small batches
    RATE_SLEEP = 7.0  # ~85 items/min ceiling well under 100

    fetched = 0
    for start in range(0, len(to_fetch_texts), B):
        batch = to_fetch_texts[start:start + B]
        indices = to_fetch_idx[start:start + B]
        # retry loop
        for attempt in range(4):
            try:
                res = client.models.embed_content(
                    model=EMBED_MODEL,
                    contents=batch,
                    config=types.EmbedContentConfig(
                        task_type=task_type,
                        output_dimensionality=EMBED_DIM,
                    ),
                )
                vecs = [list(e.values) for e in res.embeddings]
                for idx, v, t in zip(indices, vecs, batch):
                    result[idx] = v
                    cache[_key(t, task_type)] = v
                fetched += len(batch)
                break
            except Exception as e:
                msg = str(e)
                if "429" in msg or "RESOURCE_EXHAUSTED" in msg:
                    logger.warning("Rate limited on embeddings; sleeping 60s (attempt %d)", attempt + 1)
                    time.sleep(60)
                    continue
                logger.exception("Embedding batch failed: %s", e)
                raise
        # Save cache progressively so restarts don't lose progress
        if fetched % 30 == 0:
            _save_cache()
        # Throttle between batches
        if start + B < len(to_fetch_texts):
            time.sleep(RATE_SLEEP)

    _save_cache()
    return result


def embed_one(text: str, task_type: str = "RETRIEVAL_QUERY") -> List[float]:
    return embed_texts([text], task_type=task_type)[0]


def extract_use_case(free_text: str) -> dict:
    """Given free text, return {cluster, normalized_description}.

    Cluster is one of the 8 allowed labels.
    """
    prompt = f"""You are an intent classifier. The user described their main use case in one sentence.

Classify the user into EXACTLY ONE of these clusters:
- content_creation: creators, YouTubers, streamers, editors, vloggers
- gaming: gamers, esports, streaming games
- professional: office work, business, meetings, calls, freelance client work
- student: students, coursework, exams, note-taking, coding for study
- photography: photographers (pro or hobby), long shoots, RAW editing
- family_general: general family/household, kids, casual multi-use
- fitness_health: fitness, workouts, running, health tracking, meal-prep
- home_management: household admin, bills, groceries, chores, appliances

Return STRICT JSON with keys:
- cluster (one of the 8 labels above)
- normalized_description (1 short sentence rephrasing their use case)

User text: "{free_text}"
"""
    client = get_client()
    resp = _generate_with_retry(
        model=TEXT_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2,
        ),
    )
    try:
        data = json.loads(resp.text)
        cluster = data.get("cluster", "family_general")
        if cluster not in {"content_creation", "gaming", "professional", "student",
                           "photography", "family_general", "fitness_health", "home_management"}:
            cluster = "family_general"
        return {
            "cluster": cluster,
            "normalized_description": data.get("normalized_description", free_text),
        }
    except Exception as e:
        logger.exception("extract_use_case parse failed: %s", e)
        return {"cluster": "family_general", "normalized_description": free_text}


def generate_feature_cards(
    use_case_text: str,
    cluster: str,
    product_name: str,
    retrieved_specs: list,
    review_confidence: dict,
) -> list:
    """Generate personalized feature cards grounded in retrieved data.

    retrieved_specs: list of dicts with feature_name, technical_meaning,
                     benefit_template (already picked for this cluster).
    review_confidence: {feature_name: {"pct": int, "fallback": bool, "sample_size": int}}

    Returns list of {feature_name, personalized_benefit, confidence_pct,
                     confidence_fallback, sample_size}.
    """
    specs_json = json.dumps(retrieved_specs, indent=2)
    conf_json = json.dumps(review_confidence, indent=2)

    prompt = f"""You are WhyAI, an assistant that personalizes AI product features for shoppers.

The shopper is looking at: {product_name}
Their use case (raw): "{use_case_text}"
Their inferred use-case cluster: {cluster}

You are given RETRIEVED SPEC DATA for this product. Each entry has a feature_name,
technical_meaning, and a benefit_template already selected for this shopper's cluster.

You must:
- Rewrite the benefit_template into a natural, personal 1-2 sentence benefit
  addressed to the shopper (use "you" naturally). Ground your rewrite ONLY in
  the technical_meaning and benefit_template provided. Do NOT invent any new
  specification, number, or capability.
- Return one entry per feature in the SAME ORDER as the retrieved specs.
- Do NOT invent confidence scores. Confidence numbers will be attached separately.

RETRIEVED SPEC DATA:
{specs_json}

Return STRICT JSON with this shape:
{{
  "cards": [
    {{"feature_name": "...", "personalized_benefit": "1-2 sentence rewrite"}},
    ...
  ]
}}
"""
    client = get_client()
    resp = _generate_with_retry(
        model=TEXT_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.5,
        ),
    )
    try:
        data = json.loads(resp.text)
        cards = data.get("cards", [])
    except Exception as e:
        logger.exception("generate_feature_cards parse failed: %s", e)
        # Fallback: use the raw benefit templates
        cards = [{"feature_name": s["feature_name"],
                  "personalized_benefit": s["benefit_template"]}
                 for s in retrieved_specs]

    # Attach confidence data to each card
    out = []
    for card in cards:
        fname = card.get("feature_name", "")
        conf = review_confidence.get(fname, {"pct": 0, "fallback": True, "sample_size": 0, "scope": "product_overall"})
        out.append({
            "feature_name": fname,
            "personalized_benefit": card.get("personalized_benefit", ""),
            "confidence_pct": conf["pct"],
            "confidence_fallback": conf["fallback"],
            "confidence_scope": conf.get("scope", "product_overall"),
            "sample_size": conf["sample_size"],
        })
    return out


def tell_me_more(
    use_case_text: str,
    cluster: str,
    product_name: str,
    feature_name: str,
    technical_meaning: str,
    benefit_template: str,
) -> str:
    """Return a grounded 3-sentence deeper explanation of this feature."""
    prompt = f"""You are WhyAI. Explain a single product feature more deeply in EXACTLY 3 sentences.

Product: {product_name}
Feature: {feature_name}
Technical meaning (grounded — do not invent beyond this): {technical_meaning}
Benefit template for this user's cluster: {benefit_template}

User's use case: "{use_case_text}"
User's cluster: {cluster}

Write 3 sentences addressed to the user with "you". Ground everything only in the
technical_meaning and benefit_template above. Do NOT invent numbers, comparisons,
or capabilities that are not present.
Return plain text, 3 sentences.
"""
    client = get_client()
    resp = _generate_with_retry(
        model=TEXT_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.5),
    )
    return (resp.text or "").strip()

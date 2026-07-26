"""Backend tests for WhyAI — products, health, RAG-based /whyai endpoints.

NOTE: Gemini free-tier is ~5 generate_content requests/min. All LLM tests are
consolidated in one class (loadscope pins them to a single worker) and paced with
sleeps to avoid RESOURCE_EXHAUSTED errors.
"""
import os
import time
import pytest
import requests
from pymongo import MongoClient

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL") or os.environ.get("BACKEND_URL")
if not BASE_URL:
    from pathlib import Path
    envp = Path("/app/frontend/.env")
    if envp.exists():
        for line in envp.read_text().splitlines():
            if line.startswith("REACT_APP_BACKEND_URL"):
                BASE_URL = line.split("=", 1)[1].strip().strip('"')
                break
assert BASE_URL, "Missing REACT_APP_BACKEND_URL"
BASE_URL = BASE_URL.rstrip("/")

TIMEOUT = 120  # generate calls involve LLM + embeddings
LLM_SPACER = 15  # seconds between LLM generate/tell-more calls (free-tier is 5/min)


# -----------------------------
# Health / KB warm status  (no LLM)
# -----------------------------
class TestHealth:
    def test_health_kb_ready(self):
        r = requests.get(f"{BASE_URL}/api/whyai/health", timeout=30)
        assert r.status_code == 200, r.text
        data = r.json()
        assert data["kb_ready"] is True
        assert data["specs"] == 50
        assert data["reviews"] == 171

    def test_root(self):
        r = requests.get(f"{BASE_URL}/api/", timeout=30)
        assert r.status_code == 200
        d = r.json()
        assert d.get("ok") is True
        assert d.get("app") == "WhyAI"


# -----------------------------
# Products catalog  (no LLM)
# -----------------------------
class TestProducts:
    def test_get_products_list(self):
        r = requests.get(f"{BASE_URL}/api/products", timeout=30)
        assert r.status_code == 200
        data = r.json()
        assert "products" in data
        products = data["products"]
        assert len(products) == 10
        required_fields = {"id", "name", "category", "price_inr", "rating",
                           "review_count", "image", "tagline"}
        for p in products:
            assert required_fields.issubset(set(p.keys())), \
                f"Missing fields in {p.get('id')}: {required_fields - set(p.keys())}"
            assert isinstance(p["price_inr"], (int, float))
            assert isinstance(p["rating"], (int, float))
            assert isinstance(p["review_count"], int)
            assert p["image"].startswith("http")

    def test_get_product_detail_samsung(self):
        r = requests.get(f"{BASE_URL}/api/products/samsung-galaxy-s25-ultra", timeout=30)
        assert r.status_code == 200
        p = r.json()
        assert p["id"] == "samsung-galaxy-s25-ultra"
        assert "features" in p
        assert len(p["features"]) == 5
        expected_clusters = {
            "content_creation", "gaming", "professional", "student",
            "photography", "family_general", "fitness_health", "home_management",
        }
        for f in p["features"]:
            assert "feature_name" in f and "technical_meaning" in f
            assert "benefit_templates" in f
            assert set(f["benefit_templates"].keys()) == expected_clusters, \
                f"benefit_templates clusters mismatch for feature {f['feature_name']}"

    def test_get_product_detail_all_10(self):
        r = requests.get(f"{BASE_URL}/api/products", timeout=30)
        products = r.json()["products"]
        for p in products:
            rr = requests.get(f"{BASE_URL}/api/products/{p['id']}", timeout=30)
            assert rr.status_code == 200, f"Failed for {p['id']}"
            d = rr.json()
            assert len(d["features"]) == 5

    def test_get_product_detail_not_found(self):
        r = requests.get(f"{BASE_URL}/api/products/does-not-exist", timeout=30)
        assert r.status_code == 404


# -----------------------------
# All LLM-driven flows — consolidated so they run serially on one xdist worker.
# -----------------------------
class TestWhyAILLMFlow:
    # class-level shared state
    session_id = None
    feature_name = None

    def _generate(self, use_case_text, product_id):
        r = requests.post(
            f"{BASE_URL}/api/whyai/generate",
            json={"use_case_text": use_case_text, "product_id": product_id},
            timeout=TIMEOUT,
        )
        return r

    def _generate_with_retry(self, use_case_text, product_id, max_retries=2):
        """Retry once with a 45s backoff if we get a 500 that looks like Gemini 429."""
        for attempt in range(max_retries + 1):
            r = self._generate(use_case_text, product_id)
            if r.status_code == 200:
                return r
            if attempt < max_retries and r.status_code in (500, 503):
                time.sleep(45)
                continue
            return r
        return r

    def test_01_generate_content_creation(self):
        r = self._generate_with_retry(
            "I edit videos for my YouTube channel on weekends",
            "samsung-galaxy-s25-ultra",
        )
        assert r.status_code == 200, r.text
        data = r.json()
        assert "session_id" in data and data["session_id"]
        assert "use_case" in data
        assert data["use_case"]["cluster"] == "content_creation", \
            f"expected content_creation, got {data['use_case']['cluster']}"
        cards = data["cards"]
        assert len(cards) == 5
        required = {"feature_name", "personalized_benefit", "confidence_pct",
                    "confidence_fallback", "sample_size"}
        for c in cards:
            assert required.issubset(set(c.keys())), \
                f"card missing keys: {required - set(c.keys())}"
            assert isinstance(c["confidence_pct"], (int, float))
            assert isinstance(c["confidence_fallback"], bool)
            assert isinstance(c["sample_size"], int)
            assert len(c["personalized_benefit"]) > 20
        TestWhyAILLMFlow.session_id = data["session_id"]
        TestWhyAILLMFlow.feature_name = cards[0]["feature_name"]
        time.sleep(LLM_SPACER)

    def test_02_generate_family_tv(self):
        r = self._generate_with_retry(
            "We watch cricket and family movies together every evening",
            "samsung-vision-ai-qled-tv",
        )
        assert r.status_code == 200, r.text
        data = r.json()
        assert data["use_case"]["cluster"] == "family_general", \
            f"expected family_general got {data['use_case']['cluster']}"
        assert len(data["cards"]) == 5
        time.sleep(LLM_SPACER)

    def test_03_generate_fitness_watch(self):
        r = self._generate_with_retry("I run and lift 4x a week", "apple-watch-series-11")
        assert r.status_code == 200, r.text
        data = r.json()
        assert data["use_case"]["cluster"] == "fitness_health", \
            f"expected fitness_health got {data['use_case']['cluster']}"
        assert len(data["cards"]) == 5
        time.sleep(LLM_SPACER)

    def test_04_generate_bad_product(self):
        r = requests.post(
            f"{BASE_URL}/api/whyai/generate",
            json={"use_case_text": "gaming", "product_id": "not-exists"},
            timeout=TIMEOUT,
        )
        assert r.status_code == 404

    def test_05_tell_more_grounded(self):
        # Requires an LLM call — pace it
        r = requests.get(f"{BASE_URL}/api/products/samsung-galaxy-s25-ultra", timeout=30)
        feature = r.json()["features"][0]
        payload = {
            "use_case_text": "I edit videos for my YouTube channel on weekends",
            "cluster": "content_creation",
            "product_id": "samsung-galaxy-s25-ultra",
            "feature_name": feature["feature_name"],
        }
        # retry loop for 500/429
        resp = None
        for attempt in range(3):
            resp = requests.post(f"{BASE_URL}/api/whyai/tell-more", json=payload, timeout=TIMEOUT)
            if resp.status_code == 200:
                break
            time.sleep(45)
        assert resp is not None and resp.status_code == 200, resp.text if resp else "no resp"
        data = resp.json()
        assert "explanation" in data
        assert isinstance(data["explanation"], str)
        assert len(data["explanation"]) >= 100, \
            f"Explanation too short ({len(data['explanation'])}): {data['explanation']!r}"
        time.sleep(LLM_SPACER)

    def test_06_tell_more_unknown_feature(self):
        payload = {
            "use_case_text": "gaming",
            "cluster": "gaming",
            "product_id": "samsung-galaxy-s25-ultra",
            "feature_name": "Absolutely-Not-A-Real-Feature",
        }
        r = requests.post(f"{BASE_URL}/api/whyai/tell-more", json=payload, timeout=30)
        assert r.status_code == 404

    def test_07_feedback_persists_in_mongo(self):
        session_id = TestWhyAILLMFlow.session_id
        feature_name = TestWhyAILLMFlow.feature_name
        assert session_id, "session_id not captured from generate step"

        r = requests.post(
            f"{BASE_URL}/api/whyai/feedback",
            json={
                "session_id": session_id,
                "product_id": "samsung-galaxy-s25-ultra",
                "feature_name": feature_name or "any",
                "thumbs": "up",
            },
            timeout=30,
        )
        assert r.status_code == 200, r.text
        assert r.json().get("ok") is True

        # Verify in MongoDB
        mongo_url = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
        db_name = os.environ.get("DB_NAME", "test_database")
        client = MongoClient(mongo_url)
        try:
            doc = client[db_name].sessions.find_one({"id": session_id})
            assert doc is not None, "session doc missing"
            assert any(
                fb.get("thumbs") == "up" and fb.get("feature_name") == feature_name
                for fb in doc.get("feedback", [])
            ), f"Feedback not persisted: {doc.get('feedback')}"
        finally:
            client.close()

    def test_08_feedback_invalid_thumbs(self):
        r = requests.post(
            f"{BASE_URL}/api/whyai/feedback",
            json={
                "session_id": "does-not-matter",
                "product_id": "samsung-galaxy-s25-ultra",
                "feature_name": "x",
                "thumbs": "sideways",
            },
            timeout=30,
        )
        assert r.status_code == 400

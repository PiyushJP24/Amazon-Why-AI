"""Two-layer RAG: spec KB retrieval + per-feature use-case-matched review sentiment."""
from typing import List, Dict
import numpy as np


def cosine(a: List[float], b: List[float]) -> float:
    va = np.asarray(a, dtype=np.float32)
    vb = np.asarray(b, dtype=np.float32)
    denom = (np.linalg.norm(va) * np.linalg.norm(vb)) + 1e-9
    return float(np.dot(va, vb) / denom)


def retrieve_specs(
    product_id: str,
    cluster: str,
    query_vec: List[float],
    spec_entries: List[dict],
) -> List[dict]:
    """Return spec entries for this product ordered by cosine to query.
    Each returned entry includes benefit_template already selected for the cluster
    AND its own embedding (needed for per-feature review filtering).
    """
    candidates = [s for s in spec_entries if s["product_id"] == product_id]
    scored = []
    for s in candidates:
        sim = cosine(query_vec, s["embedding"])
        benefit_template = s["benefit_templates"].get(cluster) \
            or next(iter(s["benefit_templates"].values()))
        scored.append({
            "feature_name": s["feature_name"],
            "technical_meaning": s["technical_meaning"],
            "benefit_template": benefit_template,
            "embedding": s["embedding"],
            "similarity": sim,
        })
    scored.sort(key=lambda x: x["similarity"], reverse=True)
    return scored


def review_confidence_per_feature(
    product_id: str,
    cluster: str,
    query_vec: List[float],
    reviews: List[dict],
    features_with_embeddings: List[dict],
    top_k_feature: int = 7,
    min_sample: int = 4,
) -> Dict[str, dict]:
    """Per-feature two-layer RAG confidence.

      Layer 1 (feature relevance): rank all product reviews by cosine to the
              feature embedding; keep the TOP-K most feature-relevant.
      Layer 2 (use-case match): within that top-K, prefer reviews whose inferred
              cluster matches OR whose embedding is close to the user's use case.

    Falls back gracefully:
      - scope="feature+usecase": both layers found enough reviews (>=min_sample)
      - scope="feature":         layer 2 was thin, but layer 1 top-K stands
      - scope="product_overall": product has too few reviews overall — use aggregate

    Returns per-feature: {pct, sample_size, fallback, scope}
    """
    product_reviews = [r for r in reviews if r["product_id"] == product_id]
    if product_reviews:
        prod_pos = sum(1 for r in product_reviews if r["sentiment"] == "positive")
        prod_pct = round(100.0 * prod_pos / len(product_reviews))
        prod_n = len(product_reviews)
    else:
        prod_pct, prod_n = 0, 0

    # Pre-embed each product review once (they already have embeddings)
    out: Dict[str, dict] = {}
    for feat in features_with_embeddings:
        fname = feat["feature_name"]
        fvec = feat["embedding"]

        # Layer 1: TOP-K most feature-relevant reviews
        scored = [(cosine(fvec, r["embedding"]), r) for r in product_reviews]
        scored.sort(reverse=True, key=lambda x: x[0])
        feature_top = [r for _, r in scored[:top_k_feature]]

        # Layer 2: within feature_top, prefer use-case-matched reviews
        uc_pool = []
        for r in feature_top:
            cluster_match = r["inferred_use_case_cluster"] == cluster
            uc_sim = cosine(query_vec, r["embedding"])
            # Softer thresholds: cluster match OR reasonably similar to query
            if cluster_match or uc_sim >= 0.60:
                uc_pool.append(r)

        if len(uc_pool) >= min_sample:
            subset = uc_pool
            scope = "feature+usecase"
            fallback = False
        elif len(feature_top) >= min_sample:
            subset = feature_top
            scope = "feature"
            fallback = False
        elif product_reviews:
            subset = None
            scope = "product_overall"
            fallback = True
        else:
            subset = None
            scope = "product_overall"
            fallback = True

        if subset is not None:
            pos = sum(1 for r in subset if r["sentiment"] == "positive")
            pct = round(100.0 * pos / len(subset))
            n = len(subset)
        else:
            pct = prod_pct
            n = prod_n

        out[fname] = {
            "pct": pct,
            "sample_size": n,
            "fallback": fallback,
            "scope": scope,
        }
    return out

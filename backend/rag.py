"""Two-layer RAG: spec KB retrieval + use-case-matched review sentiment."""
import math
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
    """Return spec entries for this product, ordered by cosine to query.
    Each returned entry includes benefit_template already selected for the cluster.
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
            "similarity": sim,
        })
    scored.sort(key=lambda x: x["similarity"], reverse=True)
    return scored


def review_confidence_by_feature(
    product_id: str,
    cluster: str,
    query_vec: List[float],
    reviews: List[dict],
    spec_features: List[str],
    per_feature_topk: int = 8,
) -> Dict[str, dict]:
    """For each feature, compute a confidence % from the subset of reviews
    that are use-case-matched (cluster match or high similarity).

    Since our review dataset is not per-feature but per-product, we compute
    a single product-level use-case-matched confidence and apply it to every
    feature. This IS the two-layer RAG: we filter reviews by use case, then
    compute positive % over that filtered set.

    Returns: {feature_name: {pct, fallback, sample_size}}
    """
    product_reviews = [r for r in reviews if r["product_id"] == product_id]
    # Match by cluster tag (primary) AND embedding similarity (secondary support)
    cluster_matched = [r for r in product_reviews if r["inferred_use_case_cluster"] == cluster]

    # If cluster-matched pool is thin, add semantically-similar reviews
    if len(cluster_matched) < 5:
        scored = []
        for r in product_reviews:
            sim = cosine(query_vec, r["embedding"])
            scored.append((sim, r))
        scored.sort(key=lambda x: x[0], reverse=True)
        # Take top similarity reviews to fill up to 5-8
        seen_ids = {r["id"] for r in cluster_matched}
        for sim, r in scored:
            if r["id"] in seen_ids:
                continue
            if sim < 0.55:  # low similarity cutoff
                continue
            cluster_matched.append(r)
            seen_ids.add(r["id"])
            if len(cluster_matched) >= 8:
                break

    fallback = False
    matched = cluster_matched
    if len(matched) < 5:
        # fall back to overall reviews
        matched = product_reviews
        fallback = True

    if not matched:
        return {f: {"pct": 0, "fallback": True, "sample_size": 0} for f in spec_features}

    pos = sum(1 for r in matched if r["sentiment"] == "positive")
    pct = round(100.0 * pos / len(matched))
    sample_size = len(matched)

    return {
        f: {"pct": pct, "fallback": fallback, "sample_size": sample_size}
        for f in spec_features
    }

"""Pre-warm the embedding cache so backend startup is instant."""
import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

from seed_products import PRODUCTS
from seed_reviews import flatten_all_reviews
from gemini_client import embed_texts

def main():
    spec_texts = []
    for p in PRODUCTS:
        for f in p["features"]:
            spec_texts.append(f"{f['feature_name']}. {f['technical_meaning']}")
    logging.info("Embedding %d spec texts...", len(spec_texts))
    embed_texts(spec_texts, "RETRIEVAL_DOCUMENT")

    reviews = flatten_all_reviews()
    review_texts = [r["review_text"] for r in reviews]
    logging.info("Embedding %d review texts...", len(review_texts))
    embed_texts(review_texts, "RETRIEVAL_DOCUMENT")

    logging.info("Done. Cache warmed.")

if __name__ == "__main__":
    main()

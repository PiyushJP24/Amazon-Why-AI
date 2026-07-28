# WhyAI — Product Requirements & Build State

## Original problem statement
Build a full-stack web app prototype called **WhyAI** — an AI feature translator for
Amazon India's AI Store. Two parts:
1. A cloned Amazon-style product catalogue and product pages (10 real AI-powered products
   across smartphones, laptops, TVs, smartwatches, smart glasses, and home appliances).
2. A WhyAI sidebar panel that personalizes AI feature explanations using a two-layer RAG
   (spec knowledge base + review-sentiment knowledge base, both filtered by the shopper's
   stated use case).

## User personas
- Shopper who wants to understand what an AI feature *actually means for them*.
- Category-first browsers who compare across products and categories.
- Demo audience (Amazon internal review) who need a working end-to-end prototype.

## Core requirements (static)
- 10 seeded products with 5 real AI feature bullets each and per-cluster benefit templates
  across 8 use-case clusters.
- 15-18 seeded reviews per product tagged with sentiment + inferred use-case cluster.
- Two-layer RAG: (a) vector similarity over Spec KB per product, (b) cluster-match +
  vector similarity over Review KB, with % positive computed only over the use-case-matched
  subset (fallback to overall product reviews if <5 matches, transparently labelled).
- Grounded LLM generation: model must only use retrieved spec meanings/benefit templates
  and never invent confidence numbers.
- Persistent use case across product navigation (sessionStorage).
- Feedback (thumbs) and session logging in MongoDB.
- Color-coded confidence: green ≥80, yellow 60-79, orange <60.
- Tell me more → 3-sentence deeper grounded explanation.

## Tech stack
- Backend: FastAPI + Motor (MongoDB) + google-genai (Gemini 3 Flash + gemini-embedding-001)
- Frontend: React 19 + React Router + Tailwind + shadcn/ui + framer-motion + sonner
- Embeddings cached to disk at `/app/backend/data/embedding_cache.json`

## What's been implemented — 2026-02-XX (MVP)
- 10 seeded products with 5 features × 8 cluster benefit_templates each (50 specs)
- 171 paraphrased seeded reviews tagged with cluster + sentiment
- Two-layer RAG with Gemini embeddings + cosine similarity
- **Per-feature confidence** (v2): each feature card now shows its own confidence %
  computed from the top-K most feature-relevant reviews (by cosine to feature embedding),
  further filtered by use-case cluster match. Falls back through
  feature+usecase → feature-only → product_overall with clear UI copy.
- Endpoints: /api/products, /api/products/{id}, /api/whyai/generate,
  /api/whyai/tell-more, /api/whyai/feedback, /api/whyai/health
- Store rebranded to **NexKart** (marketplace shell). WhyAI is a named feature *inside*
  the store's "The AI Lab" section — never the store itself.
- New Amazon-India-style layout: dark top nav (logo/deliver-to/search/cart),
  sub-nav with "The AI Lab" badge, breadcrumb, dark hero, 6 category tiles on
  circular podium, "Explore by Use Case" tile row (6 tiles), per-category
  "Best Selling AI [Category] | Shop now" horizontal carousels.
- WhyAI sidebar: collapsed pulse tab → panel → free-text input with rotating placeholders
  → 3-step loading state → results state with feature cards
- Persistent use-case chip "Using: … · change" across product navigation
- Sonner toast on feedback
- Response cache on backend (product_id + use_case) to preserve LLM quota
- Explicit 429 handling with friendly UI toast

## Not-yet-implemented (P1 backlog)
- Per-feature review-level confidence (currently product-level aggregated). Would need
  either LLM feature-tagging on reviews or manual per-feature review labelling.
- Full Amazon-style image gallery / carousel (thumbnails currently reuse main image).
- "Compare AI features across products" flow.
- Admin dashboard showing session logs + thumbs analytics.
- Optional Emergent-managed Google auth for saving personal use cases across devices.

## Testing status
- Backend: 14/14 pytest cases pass (see /app/backend/tests/backend_test.py).
- Frontend: 7/8 UI flows verified end-to-end. The 8th (live LLM card render via browser)
  was unverified in the iteration_1 test run only because Gemini's free-tier daily
  20-generate-calls cap was already exhausted by the backend suite; the flow was verified
  manually via screenshot and via cached repeat generate calls.

## Next tasks
- P0: Enable Gemini billing (or add caching layer) so demo can run repeatedly in a day
- P1: Add per-feature review-level confidence
- P1: Compare mode across products
- P2: Analytics dashboard for admin

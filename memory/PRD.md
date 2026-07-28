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

## What's been implemented — 2026-02-XX (Iteration 3)
- **18 seeded products** (up from 10) across 6 categories: Smartphones (3), Laptops (3),
  Home Appliances (4), Televisions (3), Smartwatches (3), Smart Glasses (2). 90 total
  spec entries × 8 cluster benefit_templates each.
- **307 seeded reviews** (up from 171) tagged with cluster + sentiment.
- Store rebranded back to **Amazon.in** (portfolio prototype — Amazon wordmark + swoosh)
  while keeping WhyAI as the sidebar feature name and "The AI Lab" as the AI section.
- **Amazon.in-style PDP** with the real 3-column layout: thumbnail strip + main image (left),
  title + brand-store link + rating + "5K+ bought" + discount % + price + M.R.P + EMI +
  Offers grid (No Cost EMI, Cashback, Bank Offer, Partner Offers) + badges strip
  (10 days Service, Free Delivery, 1 Year Warranty, Pay on Delivery, Top Brand,
  Amazon Delivered) + colour swatches + spec table + About this item + Customers-keep
  green box (middle), and the buy box (Prime perk, ₹price+MRP, FREE delivery date, In stock,
  Add to Cart, Buy Now, Ships from Amazon, Sold by, Payment, Gift options,
  Add-a-Protection-Plan checkboxes, Add to Wish List) on the right.
- **Product image audit**: replaced Samsung S25 Ultra (was showing iOS), Lenovo Yoga
  (was showing a MacBook silhouette), and other placeholders with generic Unsplash
  category shots that don't leak competing OS/logo.
- Per-feature two-layer RAG confidence (from iteration 2) — every card has its own
  differentiated confidence score with scope-aware UI copy.

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

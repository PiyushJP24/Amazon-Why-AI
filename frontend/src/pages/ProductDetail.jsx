import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { fetchProduct } from "../lib/api";
import Header from "../components/Header";
import WhyAISidebar from "../components/WhyAISidebar";
import { Star, Truck, Shield, RotateCcw, ChevronRight, Sparkles } from "lucide-react";

function formatINR(n) {
  return "₹" + n.toLocaleString("en-IN");
}

export default function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetchProduct(id)
      .then((p) => setProduct(p))
      .catch(() => setProduct(null))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) {
    return (
      <div className="min-h-screen bg-white">
        <Header />
        <div className="max-w-6xl mx-auto px-4 py-10 grid md:grid-cols-2 gap-12">
          <div className="aspect-square bg-slate-100 rounded-2xl animate-pulse" />
          <div className="space-y-3">
            <div className="h-6 bg-slate-100 rounded w-2/3 animate-pulse" />
            <div className="h-4 bg-slate-100 rounded w-1/2 animate-pulse" />
            <div className="h-10 bg-slate-100 rounded w-1/3 animate-pulse" />
          </div>
        </div>
      </div>
    );
  }
  if (!product) {
    return (
      <div className="min-h-screen bg-white">
        <Header />
        <div className="max-w-4xl mx-auto p-10 text-center">
          <div className="font-store-heading text-2xl font-bold">Product not found</div>
          <Link to="/" className="text-indigo-600 mt-4 inline-block">← Back to store</Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white">
      <Header />

      {/* Breadcrumb */}
      <div className="max-w-6xl mx-auto px-4 md:px-8 py-3 text-xs text-slate-500 flex items-center gap-1">
        <Link to="/" className="hover:text-indigo-600">Store</Link>
        <ChevronRight className="w-3 h-3" />
        <span>{product.category}</span>
        <ChevronRight className="w-3 h-3" />
        <span className="text-slate-800 line-clamp-1">{product.name}</span>
      </div>

      <div className="max-w-6xl mx-auto px-4 md:px-8 pb-16 grid grid-cols-1 md:grid-cols-2 gap-10 lg:gap-14 md:pr-[440px]">
        {/* Left: Image */}
        <div>
          <div className="aspect-square rounded-3xl bg-slate-50 border border-slate-100 overflow-hidden flex items-center justify-center">
            <img
              src={product.image}
              alt={product.name}
              className="w-full h-full object-cover"
              data-testid="product-main-image"
            />
          </div>
          <div className="mt-4 flex items-center gap-3">
            {[0, 1, 2].map((i) => (
              <div key={i} className="w-16 h-16 rounded-xl border border-slate-200 bg-slate-50 flex items-center justify-center">
                <img src={product.image} alt="" className="w-full h-full object-cover rounded-xl opacity-80" />
              </div>
            ))}
          </div>
        </div>

        {/* Right: Info */}
        <div>
          <div className="inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-widest bg-gradient-to-r from-indigo-500 to-cyan-400 text-white">
            <Sparkles className="w-3 h-3" strokeWidth={2.5} /> AI Powered
          </div>
          <h1
            className="font-store-heading text-2xl md:text-3xl font-bold text-slate-900 leading-tight mt-3"
            data-testid="product-title"
          >
            {product.name}
          </h1>
          <div className="mt-2 flex items-center gap-2 text-sm">
            <div className="flex items-center gap-0.5">
              {[1, 2, 3, 4, 5].map((i) => (
                <Star
                  key={i}
                  className={`w-4 h-4 ${
                    i <= Math.round(product.rating) ? "fill-amber-400 text-amber-400" : "text-slate-300"
                  }`}
                />
              ))}
            </div>
            <span className="text-slate-500">
              {product.rating} · {product.review_count.toLocaleString("en-IN")} ratings
            </span>
          </div>

          <div className="mt-5">
            <div className="text-xs text-slate-500">M.R.P.</div>
            <div className="flex items-baseline gap-3">
              <div className="font-store-heading text-4xl font-bold text-slate-900">
                {formatINR(product.price_inr)}
              </div>
              <div className="text-sm text-slate-400 line-through">
                {formatINR(Math.round(product.price_inr * 1.15))}
              </div>
              <div className="text-sm font-semibold text-emerald-700">Save 15%</div>
            </div>
            <div className="text-xs text-slate-500 mt-1">Inclusive of all taxes · Free delivery by tomorrow</div>
          </div>

          <div className="mt-5 flex flex-wrap items-center gap-3">
            <button
              data-testid="add-to-cart"
              className="rounded-full px-6 py-2.5 bg-[#FFD814] hover:bg-[#F7CA00] text-slate-900 font-semibold text-sm active:scale-[0.98] transition-[transform,background-color]"
            >
              Add to Cart
            </button>
            <button
              data-testid="buy-now"
              className="rounded-full px-6 py-2.5 bg-[#FF9900] hover:bg-[#E68A00] text-white font-semibold text-sm active:scale-[0.98] transition-[transform,background-color]"
            >
              Buy Now
            </button>
          </div>

          <div className="mt-6 grid grid-cols-3 gap-3 text-xs text-slate-600">
            <div className="flex items-center gap-2 rounded-xl border border-slate-100 p-2.5">
              <Truck className="w-4 h-4 text-slate-500" /> Free delivery
            </div>
            <div className="flex items-center gap-2 rounded-xl border border-slate-100 p-2.5">
              <Shield className="w-4 h-4 text-slate-500" /> 1yr warranty
            </div>
            <div className="flex items-center gap-2 rounded-xl border border-slate-100 p-2.5">
              <RotateCcw className="w-4 h-4 text-slate-500" /> 7-day return
            </div>
          </div>

          {/* About this item */}
          <div className="mt-8 rounded-2xl bg-slate-50 border border-slate-100 p-5">
            <div className="font-store-heading text-lg font-bold text-slate-900">About this item</div>
            <ul className="mt-3 space-y-2.5" data-testid="feature-bullets">
              {product.features.map((f, i) => (
                <li key={i} className="flex gap-2 text-[14px] leading-snug text-slate-700">
                  <span className="mt-1.5 w-1 h-1 rounded-full bg-slate-400 shrink-0" />
                  <span>
                    <span className="font-semibold text-slate-900">{f.feature_name}:</span>{" "}
                    <span>{f.technical_meaning}</span>
                  </span>
                </li>
              ))}
            </ul>
            <div className="mt-4 rounded-xl bg-white border border-indigo-100 p-3 text-[13px] text-slate-700 flex items-start gap-2">
              <Sparkles className="w-4 h-4 text-indigo-500 mt-0.5 shrink-0" />
              <span>
                <span className="font-whyai font-semibold text-indigo-700">Want this in plain English for you?</span>{" "}
                Open WhyAI on the right — one sentence about how you'll use this, and every feature above becomes personal.
              </span>
            </div>
          </div>
        </div>
      </div>

      <WhyAISidebar product={product} />
    </div>
  );
}

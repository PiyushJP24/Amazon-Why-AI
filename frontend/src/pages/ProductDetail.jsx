import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { fetchProduct } from "../lib/api";
import Header from "../components/Header";
import WhyAISidebar from "../components/WhyAISidebar";
import { Star, Truck, Shield, RotateCcw, ChevronRight, Sparkles, Check } from "lucide-react";

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
      <div className="min-h-screen bg-slate-100">
        <Header />
        <div className="max-w-[1400px] mx-auto px-4 py-10 grid md:grid-cols-2 gap-12">
          <div className="aspect-square bg-white rounded-md animate-pulse" />
          <div className="space-y-3">
            <div className="h-6 bg-white rounded w-2/3 animate-pulse" />
            <div className="h-4 bg-white rounded w-1/2 animate-pulse" />
            <div className="h-10 bg-white rounded w-1/3 animate-pulse" />
          </div>
        </div>
      </div>
    );
  }
  if (!product) {
    return (
      <div className="min-h-screen bg-slate-100">
        <Header />
        <div className="max-w-4xl mx-auto p-10 text-center bg-white rounded-md mt-6">
          <div className="font-store-heading text-2xl font-bold">Product not found</div>
          <Link to="/" className="text-indigo-600 mt-4 inline-block">← Back to store</Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      {/* Breadcrumb */}
      <div className="max-w-[1400px] mx-auto px-4 md:px-5 py-2.5 text-xs text-slate-500 flex items-center gap-1 flex-wrap">
        <Link to="/" className="hover:text-indigo-600">NexKart</Link>
        <ChevronRight className="w-3 h-3" />
        <Link to="/" className="hover:text-indigo-600">The AI Lab</Link>
        <ChevronRight className="w-3 h-3" />
        <span>{product.category}</span>
        <ChevronRight className="w-3 h-3" />
        <span className="text-slate-800 line-clamp-1 truncate">{product.name}</span>
      </div>

      <div className="max-w-[1400px] mx-auto px-4 md:px-5 pb-16 md:pr-[440px]">
        <div className="bg-white rounded-md p-4 md:p-6 grid grid-cols-1 md:grid-cols-[minmax(0,1fr)_minmax(0,1.15fr)] gap-8 lg:gap-12">
          {/* Left: Image */}
          <div>
            <div className="aspect-square rounded-md bg-white border border-slate-100 overflow-hidden flex items-center justify-center">
              <img
                src={product.image}
                alt={product.name}
                className="w-full h-full object-cover"
                data-testid="product-main-image"
              />
            </div>
            <div className="mt-3 flex items-center gap-2">
              {[0, 1, 2, 3].map((i) => (
                <div key={i} className="w-14 h-14 rounded-md border border-slate-200 bg-white flex items-center justify-center overflow-hidden">
                  <img src={product.image} alt="" className="w-full h-full object-cover opacity-90" />
                </div>
              ))}
            </div>
          </div>

          {/* Right: Info */}
          <div>
            <div className="inline-flex items-center gap-1 rounded px-2 py-0.5 text-[10px] font-semibold uppercase tracking-widest bg-gradient-to-r from-indigo-500 to-cyan-400 text-white">
              <Sparkles className="w-3 h-3" strokeWidth={2.5} /> The AI Lab
            </div>
            <h1
              className="font-store-heading text-2xl md:text-[26px] font-semibold text-slate-900 leading-snug mt-2.5"
              data-testid="product-title"
            >
              {product.name}
            </h1>
            <div className="mt-1 text-sm text-slate-600">
              Brand: <span className="text-indigo-700 hover:underline cursor-pointer">{product.brand}</span>
            </div>
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
              <span className="text-indigo-700">{product.rating}</span>
              <span className="text-slate-400">|</span>
              <span className="text-indigo-700 hover:underline cursor-pointer">{product.review_count.toLocaleString("en-IN")} ratings</span>
            </div>

            <hr className="my-4 border-slate-100" />

            <div>
              <div className="text-xs text-slate-500">Deal Price</div>
              <div className="flex items-baseline gap-3 mt-0.5">
                <div className="font-store-heading text-[28px] leading-none">
                  <span className="text-[16px] align-top text-slate-700">₹</span>
                  <span className="font-bold text-slate-900">{product.price_inr.toLocaleString("en-IN")}</span>
                  <sup className="text-[13px] font-semibold ml-0.5">00</sup>
                </div>
                <div className="text-sm text-slate-500">
                  M.R.P: <span className="line-through">{formatINR(Math.round(product.price_inr * 1.15))}</span>
                </div>
                <div className="text-sm font-semibold text-red-600">(15% off)</div>
              </div>
              <div className="text-xs text-slate-500 mt-1">Inclusive of all taxes</div>
              <div className="text-sm text-emerald-700 font-semibold mt-2 flex items-center gap-1">
                <Check className="w-4 h-4" /> In stock · Free delivery by tomorrow
              </div>
            </div>

            <hr className="my-4 border-slate-100" />

            <div className="flex flex-wrap items-center gap-3">
              <button
                data-testid="add-to-cart"
                className="rounded-full px-6 py-2.5 bg-amber-400 hover:bg-amber-500 text-slate-900 font-semibold text-sm active:scale-[0.98] transition-[transform,background-color]"
              >
                Add to Cart
              </button>
              <button
                data-testid="buy-now"
                className="rounded-full px-6 py-2.5 bg-orange-500 hover:bg-orange-600 text-white font-semibold text-sm active:scale-[0.98] transition-[transform,background-color]"
              >
                Buy Now
              </button>
            </div>

            <div className="mt-5 grid grid-cols-3 gap-2 text-[11px] text-slate-600">
              <div className="flex items-center gap-1.5 rounded-md border border-slate-200 p-2">
                <Truck className="w-4 h-4 text-slate-500" /> Free delivery
              </div>
              <div className="flex items-center gap-1.5 rounded-md border border-slate-200 p-2">
                <Shield className="w-4 h-4 text-slate-500" /> 1yr warranty
              </div>
              <div className="flex items-center gap-1.5 rounded-md border border-slate-200 p-2">
                <RotateCcw className="w-4 h-4 text-slate-500" /> 7-day return
              </div>
            </div>

            {/* About this item */}
            <div className="mt-6 rounded-md bg-slate-50 border border-slate-100 p-4">
              <div className="font-store-heading text-base font-bold text-slate-900 mb-2">About this item</div>
              <ul className="space-y-2" data-testid="feature-bullets">
                {product.features.map((f, i) => (
                  <li key={i} className="flex gap-2 text-[13.5px] leading-snug text-slate-700">
                    <span className="mt-1.5 w-1 h-1 rounded-full bg-slate-500 shrink-0" />
                    <span>
                      <span className="font-semibold text-slate-900">{f.feature_name}:</span>{" "}
                      <span>{f.technical_meaning}</span>
                    </span>
                  </li>
                ))}
              </ul>
              <div className="mt-4 rounded-md bg-white border border-indigo-100 p-2.5 text-[13px] text-slate-700 flex items-start gap-2">
                <Sparkles className="w-4 h-4 text-indigo-500 mt-0.5 shrink-0" />
                <span>
                  <span className="font-whyai font-semibold text-indigo-700">Want this in plain English for you?</span>{" "}
                  Open the WhyAI panel on the right — one sentence about how you'll use this, and every feature above becomes personal.
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <WhyAISidebar product={product} />
    </div>
  );
}

import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchProducts } from "../lib/api";
import ProductCard from "../components/ProductCard";
import Header from "../components/Header";
import { Sparkles, ArrowRight } from "lucide-react";

export default function Home() {
  const [products, setProducts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("all");
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetchProducts()
      .then((data) => setProducts(data.products || []))
      .catch(() => setProducts([]))
      .finally(() => setLoading(false));
  }, []);

  const filtered = useMemo(() => {
    if (selectedCategory === "all") return products;
    return products.filter((p) => p.category === selectedCategory);
  }, [products, selectedCategory]);

  return (
    <div className="min-h-screen bg-white">
      <Header
        selectedCategory={selectedCategory}
        onSelectCategory={setSelectedCategory}
      />

      {/* Hero */}
      <section className="border-b border-slate-100 bg-gradient-to-br from-indigo-50 via-white to-cyan-50">
        <div className="max-w-7xl mx-auto px-4 md:px-8 py-10 md:py-14 grid md:grid-cols-2 gap-10 items-center">
          <div>
            <div className="inline-flex items-center gap-1.5 rounded-full bg-white shadow-sm border border-indigo-100 px-3 py-1 text-xs font-medium text-indigo-700">
              <Sparkles className="w-3.5 h-3.5" /> New · The AI Store, translated for you
            </div>
            <h1
              className="font-store-heading text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-slate-900 mt-4 leading-[1.05]"
              data-testid="hero-title"
            >
              Every AI feature.<br />
              <span className="bg-gradient-to-r from-indigo-500 to-cyan-500 bg-clip-text text-transparent">
                Explained for how <em>you</em> live.
              </span>
            </h1>
            <p className="text-slate-600 mt-4 max-w-lg text-[15px] leading-relaxed">
              Tap any product below. Tell WhyAI how you'll actually use it, and see every AI
              feature rewritten just for you — grounded in what real buyers say.
            </p>
            <div className="mt-6 flex items-center gap-3">
              <button
                data-testid="hero-cta"
                onClick={() => document.getElementById("catalog")?.scrollIntoView({ behavior: "smooth" })}
                className="rounded-full bg-slate-900 hover:bg-slate-800 text-white px-5 py-2.5 text-sm font-semibold inline-flex items-center gap-2 active:scale-[0.98] transition-[transform,background-color]"
              >
                Browse the AI Store <ArrowRight className="w-4 h-4" />
              </button>
              <div className="text-xs text-slate-500">10 AI-powered products · Real reviews · Live RAG</div>
            </div>
          </div>

          <div className="relative">
            <div className="rounded-3xl bg-white shadow-xl ring-1 ring-slate-100 p-6">
              <div className="flex items-center gap-2 mb-3">
                <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-indigo-500 to-cyan-400 flex items-center justify-center">
                  <Sparkles className="w-4 h-4 text-white" strokeWidth={2.4} />
                </div>
                <div className="font-whyai font-bold text-slate-900">WhyAI · Preview</div>
              </div>
              <div className="rounded-xl bg-indigo-50 text-indigo-800 px-3 py-2 text-[13px] font-whyai border border-indigo-100">
                Using: I edit videos for my YouTube channel on weekends
              </div>
              <div className="mt-3 rounded-xl border border-slate-100 p-3">
                <div className="text-[10px] font-semibold uppercase tracking-widest text-indigo-600">200MP AI ProVisual Engine</div>
                <div className="text-[14px] mt-1 text-slate-800 font-whyai leading-snug">
                  Shoot crisp 4K vlogs and cinematic B-roll from ultrawide to 100x zoom without ever switching lenses.
                </div>
                <div className="mt-2 inline-flex items-center gap-1.5 text-[11px] rounded-full px-2 py-0.5 bg-emerald-50 text-emerald-800 border border-emerald-200">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
                  89% of creators with a similar use case rated this positively
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Catalog */}
      <section id="catalog" className="max-w-7xl mx-auto px-4 md:px-8 py-10">
        <div className="flex items-end justify-between mb-6">
          <div>
            <div className="text-xs uppercase font-semibold tracking-wide text-indigo-600">The AI Store</div>
            <h2 className="font-store-heading text-2xl md:text-3xl font-bold text-slate-900 mt-1">
              {selectedCategory === "all" ? "All AI-Powered Picks" : selectedCategory}
            </h2>
          </div>
          <div className="text-sm text-slate-500 hidden md:block">
            {filtered.length} product{filtered.length === 1 ? "" : "s"}
          </div>
        </div>

        {loading ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {Array.from({ length: 8 }).map((_, i) => (
              <div key={i} className="rounded-2xl border border-slate-100 p-4">
                <div className="aspect-square rounded-xl bg-slate-100 animate-pulse mb-4" />
                <div className="h-3 bg-slate-100 rounded w-1/3 animate-pulse mb-2" />
                <div className="h-4 bg-slate-100 rounded w-2/3 animate-pulse mb-2" />
                <div className="h-6 bg-slate-100 rounded w-1/3 animate-pulse" />
              </div>
            ))}
          </div>
        ) : (
          <div
            data-testid="product-grid"
            className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6"
          >
            {filtered.map((p) => (
              <ProductCard key={p.id} product={p} />
            ))}
          </div>
        )}
      </section>

      <footer className="border-t border-slate-100 py-8 mt-6">
        <div className="max-w-7xl mx-auto px-4 md:px-8 text-xs text-slate-500 flex flex-wrap items-center justify-between gap-3">
          <div>© WhyAI Demo Store · A prototype for the Amazon India AI Store</div>
          <div className="flex items-center gap-1">
            <Sparkles className="w-3 h-3 text-indigo-500" />
            Grounded generation · two-layer RAG · Gemini
          </div>
        </div>
      </footer>
    </div>
  );
}

import { useEffect, useMemo, useState, useRef } from "react";
import { Link } from "react-router-dom";
import { fetchProducts } from "../lib/api";
import ProductCard from "../components/ProductCard";
import CategoryTile from "../components/CategoryTile";
import Header from "../components/Header";
import { ChevronRight, ChevronLeft, Sparkles, Languages, ImagePlus, Mic, ShieldCheck, Battery, GraduationCap, Zap } from "lucide-react";

const CATEGORIES = ["Smartphones", "Laptops", "Home Appliances", "Televisions", "Smartwatches", "Smart Glasses"];

const USECASE_TILES = [
  { label: "Real-Time Voice Translation", Icon: Languages, color: "from-fuchsia-400 to-amber-300" },
  { label: "Generative Editing", Icon: ImagePlus, color: "from-cyan-400 to-blue-500" },
  { label: "Smart Assistance & Productivity", Icon: Mic, color: "from-sky-400 to-indigo-500" },
  { label: "On-Device AI. Maintain Data Privacy", Icon: ShieldCheck, color: "from-violet-500 to-fuchsia-500" },
  { label: "Intelligent Battery Life", Icon: Battery, color: "from-lime-400 to-emerald-500" },
  { label: "AI-Powered Learning", Icon: GraduationCap, color: "from-orange-400 to-rose-400" },
];

function Carousel({ products }) {
  const scrollerRef = useRef(null);
  const scroll = (dir) => {
    const el = scrollerRef.current;
    if (!el) return;
    el.scrollBy({ left: dir * el.clientWidth * 0.85, behavior: "smooth" });
  };
  return (
    <div className="relative">
      <button
        onClick={() => scroll(-1)}
        className="hidden md:flex absolute -left-3 top-1/2 -translate-y-1/2 z-10 w-9 h-9 bg-white shadow-md border border-slate-200 rounded-full items-center justify-center hover:bg-slate-50 transition-colors"
        aria-label="Scroll left"
      >
        <ChevronLeft className="w-4 h-4 text-slate-700" />
      </button>
      <div
        ref={scrollerRef}
        className="flex gap-3 overflow-x-auto no-scrollbar snap-x snap-mandatory pb-2"
      >
        {products.map((p) => (
          <div key={p.id} className="shrink-0 w-[190px] sm:w-[220px] snap-start">
            <ProductCard product={p} />
          </div>
        ))}
      </div>
      <button
        onClick={() => scroll(1)}
        className="hidden md:flex absolute -right-3 top-1/2 -translate-y-1/2 z-10 w-9 h-9 bg-white shadow-md border border-slate-200 rounded-full items-center justify-center hover:bg-slate-50 transition-colors"
        aria-label="Scroll right"
      >
        <ChevronRight className="w-4 h-4 text-slate-700" />
      </button>
    </div>
  );
}

export default function Home() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeCategory, setActiveCategory] = useState("Smartphones");

  useEffect(() => {
    fetchProducts()
      .then((data) => setProducts(data.products || []))
      .catch(() => setProducts([]))
      .finally(() => setLoading(false));
  }, []);

  const byCategory = useMemo(() => {
    const m = {};
    CATEGORIES.forEach((c) => (m[c] = []));
    products.forEach((p) => {
      if (m[p.category]) m[p.category].push(p);
      else if (p.category === "Home Appliances") m["Home Appliances"].push(p);
    });
    return m;
  }, [products]);

  const scrollToCategory = (cat) => {
    setActiveCategory(cat);
    const el = document.getElementById(`section-${cat.replace(/\s+/g, "-")}`);
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
  };

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      {/* Breadcrumb */}
      <div className="max-w-[1400px] mx-auto px-3 md:px-5 pt-3 text-[12px] text-slate-500 flex items-center gap-1">
        <span>Category</span>
        <ChevronRight className="w-3 h-3" />
        <span className="hover:text-indigo-600 cursor-pointer">Consumer Electronics</span>
        <ChevronRight className="w-3 h-3" />
        <span className="text-slate-900 font-medium">The AI Lab</span>
      </div>

      <div className="max-w-[1400px] mx-auto px-3 md:px-5 py-4">
        {/* Hero */}
        <section className="relative overflow-hidden rounded-xl bg-[#0B0F1A] text-white">
          <div className="absolute inset-0 opacity-70">
            <div className="absolute -bottom-40 left-1/2 -translate-x-1/2 w-[800px] h-[400px] rounded-full bg-gradient-to-t from-indigo-500/70 via-cyan-400/40 to-transparent blur-2xl" />
          </div>
          <div className="relative py-14 md:py-20 px-6 flex flex-col items-center text-center">
            <div className="inline-flex items-center gap-1.5 rounded-full bg-white/10 backdrop-blur border border-white/20 px-3 py-1 text-[11px] font-medium tracking-wide">
              <Sparkles className="w-3 h-3" /> The AI Lab · Powered by WhyAI
            </div>
            <h1
              data-testid="hero-title"
              className="font-store-heading text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tighter mt-5 bg-gradient-to-b from-white to-slate-300 bg-clip-text text-transparent"
            >
              The AI Lab
            </h1>
            <p className="mt-2 text-lg sm:text-xl font-store-heading font-light text-slate-200">
              Your Intelligence Upgrade
            </p>
            <button
              data-testid="hero-cta"
              onClick={() => scrollToCategory("Smartphones")}
              className="mt-8 rounded-full px-6 py-2.5 bg-white text-slate-900 font-semibold text-sm hover:bg-slate-100 active:scale-[0.98] transition-[transform,background-color]"
            >
              Explore AI-powered devices
            </button>
          </div>
        </section>

        {/* Category tiles */}
        <section className="mt-6 rounded-xl bg-white p-5 shadow-sm">
          <div className="grid grid-cols-3 sm:grid-cols-6 gap-4">
            {CATEGORIES.map((c) => (
              <CategoryTile
                key={c}
                category={c}
                active={activeCategory === c}
                onClick={() => scrollToCategory(c)}
              />
            ))}
          </div>
        </section>

        {/* Explore by Usecase — like Amazon's tile row */}
        <section className="mt-6 rounded-xl bg-[#0B0F1A] text-white p-5 md:p-7">
          <div className="flex items-baseline justify-between mb-4">
            <h2 className="font-store-heading text-xl md:text-2xl font-bold tracking-tight">
              Explore by Use Case
            </h2>
            <div className="text-[12px] text-slate-400 hidden sm:block">
              WhyAI translates every one of these for you
            </div>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
            {USECASE_TILES.map(({ label, Icon, color }) => (
              <div
                key={label}
                data-testid={`usecase-tile-${label}`}
                className="flex flex-col items-center gap-2 group cursor-pointer"
              >
                <div className="relative">
                  <div className="absolute inset-x-2 -bottom-1 h-3 rounded-[50%] bg-black/60 blur-[3px]" />
                  <div className="relative w-20 h-20 rounded-full bg-slate-200 flex items-center justify-center shadow-md ring-2 ring-slate-700 group-hover:ring-indigo-400 transition-shadow">
                    <div className={`w-11 h-11 rounded-full bg-gradient-to-br ${color} flex items-center justify-center`}>
                      <Icon className="w-6 h-6 text-white" strokeWidth={1.8} />
                    </div>
                  </div>
                </div>
                <div className="text-[12px] text-center font-semibold leading-tight max-w-[110px]">
                  {label}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Per-category "Best Selling AI [Category]" sections */}
        {loading ? (
          <div className="mt-8 grid grid-cols-2 sm:grid-cols-4 gap-4">
            {Array.from({ length: 8 }).map((_, i) => (
              <div key={i} className="bg-white rounded-md p-3">
                <div className="aspect-square bg-slate-100 animate-pulse rounded" />
                <div className="h-3 bg-slate-100 rounded mt-3 w-2/3 animate-pulse" />
                <div className="h-4 bg-slate-100 rounded mt-2 w-1/2 animate-pulse" />
              </div>
            ))}
          </div>
        ) : (
          CATEGORIES.map((cat) => {
            const items = byCategory[cat] || [];
            if (items.length === 0) return null;
            return (
              <section
                key={cat}
                id={`section-${cat.replace(/\s+/g, "-")}`}
                className="mt-6 rounded-xl bg-white p-5 shadow-sm scroll-mt-32"
              >
                <div className="flex items-baseline justify-between mb-4 border-b border-slate-100 pb-3">
                  <h2 className="font-store-heading text-xl md:text-2xl font-bold text-slate-900">
                    Best Selling AI {cat}
                    <span className="text-slate-400 font-normal"> | Shop now</span>
                  </h2>
                  <Link
                    to="/"
                    className="text-sm text-indigo-600 hover:text-indigo-700 hidden sm:inline"
                  >
                    See all
                  </Link>
                </div>
                <Carousel products={items} />
              </section>
            );
          })
        )}

        {/* WhyAI feature callout at the bottom */}
        <section className="mt-6 rounded-xl overflow-hidden bg-gradient-to-r from-indigo-600 via-indigo-500 to-cyan-400 text-white">
          <div className="p-6 md:p-8 flex flex-col md:flex-row items-center gap-6">
            <div className="w-14 h-14 rounded-2xl bg-white/15 backdrop-blur border border-white/20 flex items-center justify-center shrink-0">
              <Sparkles className="w-7 h-7" />
            </div>
            <div className="flex-1">
              <div className="text-[11px] uppercase tracking-widest font-semibold text-white/80">
                Introducing WhyAI
              </div>
              <h3 className="font-store-heading text-xl md:text-2xl font-bold mt-1">
                On every product, click the WhyAI tab to see what each AI feature means for you.
              </h3>
              <p className="text-white/85 mt-1 text-sm max-w-2xl">
                Type one sentence about how you'll actually use the device. WhyAI translates every
                AI feature into your world, grounded in real buyer reviews with a similar use case.
              </p>
            </div>
          </div>
        </section>
      </div>

      <footer className="border-t border-slate-200 py-8 mt-6 bg-white">
        <div className="max-w-[1400px] mx-auto px-3 md:px-5 text-xs text-slate-500 flex flex-wrap items-center justify-between gap-3">
          <div>© NexKart · The AI Lab prototype</div>
          <div className="flex items-center gap-1">
            <Zap className="w-3 h-3 text-amber-500" />
            WhyAI · two-layer RAG · Gemini
          </div>
        </div>
      </footer>
    </div>
  );
}

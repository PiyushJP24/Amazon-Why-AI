import { Link, useLocation } from "react-router-dom";
import { Search, ShoppingCart, MapPin, Sparkles } from "lucide-react";

const CATEGORIES = [
  { label: "All", value: "all" },
  { label: "Smartphones", value: "Smartphones" },
  { label: "Laptops", value: "Laptops" },
  { label: "Televisions", value: "Televisions" },
  { label: "Smartwatches", value: "Smartwatches" },
  { label: "Smart Glasses", value: "Smart Glasses" },
  { label: "Home Appliances", value: "Home Appliances" },
];

export default function Header({ selectedCategory, onSelectCategory }) {
  const location = useLocation();
  const isHome = location.pathname === "/";
  return (
    <header data-testid="site-header" className="w-full border-b border-slate-200 bg-white sticky top-0 z-40">
      <div className="max-w-7xl mx-auto px-4 md:px-8 py-3 flex items-center gap-6">
        <Link to="/" data-testid="header-logo" className="flex items-center gap-2 shrink-0">
          <div className="w-9 h-9 rounded-lg bg-gradient-to-tr from-indigo-500 to-cyan-400 flex items-center justify-center shadow-sm">
            <Sparkles className="w-5 h-5 text-white" strokeWidth={2.4} />
          </div>
          <div className="font-store-heading font-bold text-slate-900 text-lg md:text-xl leading-none">
            WhyAI <span className="text-slate-500 font-medium">Demo Store</span>
          </div>
        </Link>

        <div className="hidden md:flex items-center gap-2 text-sm text-slate-600 shrink-0">
          <MapPin className="w-4 h-4" />
          <div>
            <div className="text-[11px] leading-none text-slate-400">Deliver to</div>
            <div className="font-medium leading-tight">Bengaluru 560001</div>
          </div>
        </div>

        <div className="flex-1 max-w-2xl">
          <div className="flex items-center rounded-full border border-slate-200 focus-within:ring-2 focus-within:ring-indigo-400 focus-within:border-indigo-400 transition-colors bg-white overflow-hidden">
            <input
              data-testid="header-search"
              type="text"
              placeholder="Search AI products, features, brands..."
              className="flex-1 px-5 py-2.5 text-sm bg-transparent outline-none"
            />
            <button className="bg-[#FF9900] hover:bg-[#E68A00] active:scale-[0.98] transition-colors text-white p-2.5 px-4 rounded-r-full">
              <Search className="w-4 h-4" />
            </button>
          </div>
        </div>

        <button data-testid="header-cart" className="hidden md:flex items-center gap-2 text-sm text-slate-700 hover:text-slate-900 transition-colors">
          <ShoppingCart className="w-5 h-5" />
          <span className="font-medium">Cart</span>
        </button>
      </div>

      {isHome && (
        <div className="border-t border-slate-100 bg-slate-50">
          <div className="max-w-7xl mx-auto px-4 md:px-8 flex items-center gap-1 overflow-x-auto no-scrollbar py-2">
            {CATEGORIES.map((c) => (
              <button
                key={c.value}
                data-testid={`cat-tab-${c.value}`}
                onClick={() => onSelectCategory?.(c.value)}
                className={`shrink-0 px-4 py-1.5 rounded-full text-sm font-medium transition-colors ${
                  selectedCategory === c.value
                    ? "bg-slate-900 text-white"
                    : "text-slate-700 hover:bg-white hover:text-slate-900"
                }`}
              >
                {c.label}
              </button>
            ))}
          </div>
        </div>
      )}
    </header>
  );
}

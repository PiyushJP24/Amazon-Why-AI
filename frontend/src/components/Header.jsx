import { Link, useLocation } from "react-router-dom";
import { Search, ShoppingCart, MapPin, ChevronDown, Menu, Zap } from "lucide-react";

// Primary top-nav categories (like Amazon's black-bar subnav)
const NAV_CATS = [
  { label: "All", to: "/", key: "all" },
  { label: "Today's Deals", to: "/", key: "deals" },
  { label: "Mobiles", to: "/", key: "mobiles" },
  { label: "Electronics", to: "/", key: "electronics" },
  { label: "Home & Kitchen", to: "/", key: "home" },
  { label: "Computers", to: "/", key: "computers" },
];

export default function Header() {
  return (
    <header data-testid="site-header" className="w-full sticky top-0 z-40 shadow-sm">
      {/* Top bar (Amazon-style navy) */}
      <div className="bg-[#131A22] text-white">
        <div className="max-w-[1500px] mx-auto px-3 md:px-5 py-2 flex items-center gap-3 md:gap-4">
          <Link
            to="/"
            data-testid="header-logo"
            className="flex items-end shrink-0 border border-transparent hover:border-white/40 rounded-md px-2 py-1 transition-colors -mb-0.5"
          >
            <div className="font-store-heading font-extrabold text-[26px] leading-none tracking-tight text-white lowercase relative">
              amazon
              <svg
                viewBox="0 0 100 20"
                className="absolute -bottom-1.5 left-2 w-[85%] h-3 text-amber-500"
                fill="none"
                stroke="currentColor"
                strokeWidth="3"
                strokeLinecap="round"
              >
                <path d="M2 6 Q 50 22, 95 4" />
                <path d="M88 2 L 95 4 L 90 10" strokeWidth="2.5" />
              </svg>
            </div>
            <span className="text-[13px] font-medium text-white ml-0.5 leading-none pb-0.5">.in</span>
          </Link>

          <button className="hidden md:flex items-center gap-1 shrink-0 text-xs text-slate-200 hover:border-white border border-transparent rounded-md px-2 py-1 transition-colors">
            <MapPin className="w-4 h-4 text-slate-400" />
            <div className="text-left">
              <div className="text-[10px] leading-none text-slate-400">Deliver to</div>
              <div className="text-[13px] font-semibold leading-tight">Bengaluru 560001</div>
            </div>
          </button>

          <div className="flex-1 min-w-0">
            <div className="flex items-center rounded-md bg-white text-slate-900 overflow-hidden focus-within:ring-2 focus-within:ring-amber-400">
              <div className="hidden sm:flex items-center gap-1 px-3 border-r border-slate-200 bg-slate-100 text-xs font-medium text-slate-600 h-full">
                All <ChevronDown className="w-3 h-3" />
              </div>
              <input
                data-testid="header-search"
                type="text"
                placeholder="Search Amazon.in"
                className="flex-1 px-3 py-2 text-sm outline-none min-w-0"
              />
              <button className="bg-amber-400 hover:bg-amber-500 active:scale-[0.98] transition-[background-color,transform] px-4 h-full py-2.5">
                <Search className="w-4 h-4 text-slate-900" />
              </button>
            </div>
          </div>

          <button className="hidden md:flex flex-col items-start shrink-0 text-white text-xs hover:border-white border border-transparent rounded-md px-2 py-1 transition-colors">
            <span className="text-[11px] text-slate-300 leading-none">Hello, sign in</span>
            <span className="font-semibold text-[13px] leading-tight flex items-center gap-0.5">
              Account & Lists <ChevronDown className="w-3 h-3" />
            </span>
          </button>

          <Link
            to="/"
            data-testid="header-cart"
            className="flex items-center gap-1 shrink-0 hover:border-white border border-transparent rounded-md px-2 py-1 transition-colors"
          >
            <div className="relative">
              <ShoppingCart className="w-6 h-6" />
              <span className="absolute -top-1.5 -right-2 bg-amber-400 text-slate-900 text-[10px] font-bold rounded-full w-4 h-4 flex items-center justify-center">
                0
              </span>
            </div>
            <span className="font-semibold text-sm hidden sm:inline">Cart</span>
          </Link>
        </div>
      </div>

      {/* Sub-nav (Amazon-style slightly lighter) */}
      <div className="bg-[#232F3E] text-slate-100">
        <div className="max-w-[1500px] mx-auto px-3 md:px-5 flex items-center gap-1 overflow-x-auto no-scrollbar py-1.5">
          <button className="flex items-center gap-1 px-2 py-1 text-[13px] font-medium hover:border-white border border-transparent rounded-md transition-colors">
            <Menu className="w-4 h-4" /> All
          </button>
          {NAV_CATS.slice(1).map((c) => (
            <button
              key={c.key}
              className="shrink-0 px-2 py-1 text-[13px] hover:border-white border border-transparent rounded-md transition-colors"
            >
              {c.label}
            </button>
          ))}
          <Link
            to="/"
            data-testid="nav-ai-lab"
            className="shrink-0 ml-1 px-2.5 py-1 text-[13px] font-semibold bg-gradient-to-r from-indigo-500 to-cyan-400 text-white rounded-md flex items-center gap-1 hover:shadow-md transition-shadow"
          >
            <Zap className="w-3.5 h-3.5" fill="currentColor" strokeWidth={0} />
            The AI Lab
          </Link>
        </div>
      </div>
    </header>
  );
}

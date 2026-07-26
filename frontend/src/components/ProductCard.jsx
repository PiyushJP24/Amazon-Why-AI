import { Link } from "react-router-dom";
import { Star, Sparkles } from "lucide-react";

function formatINR(n) {
  return "₹" + n.toLocaleString("en-IN");
}

export default function ProductCard({ product }) {
  return (
    <Link
      to={`/product/${product.id}`}
      data-testid={`product-card-${product.id}`}
      className="group relative flex flex-col rounded-2xl border border-slate-200 bg-white p-4 hover:shadow-md hover:-translate-y-0.5 hover:border-slate-300 transition-[transform,box-shadow,border-color] duration-200"
    >
      <div className="absolute top-3 right-3 z-10">
        <div className="flex items-center gap-1 rounded-full px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wide bg-gradient-to-r from-indigo-500 to-cyan-400 text-white shadow-sm">
          <Sparkles className="w-3 h-3" strokeWidth={2.5} />
          AI Powered
        </div>
      </div>

      <div className="aspect-square rounded-xl bg-slate-50 flex items-center justify-center overflow-hidden mb-4">
        <img
          src={product.image}
          alt={product.name}
          className="w-full h-full object-cover group-hover:scale-[1.03] transition-transform duration-500"
          loading="lazy"
        />
      </div>

      <div className="flex-1 flex flex-col">
        <div className="text-[11px] text-slate-500 uppercase tracking-wide">{product.category}</div>
        <div className="font-store-heading font-semibold text-slate-900 text-[15px] leading-snug line-clamp-2 mt-1">
          {product.name}
        </div>
        <div className="text-xs text-slate-500 mt-1 line-clamp-1">{product.tagline}</div>

        <div className="mt-3 flex items-center gap-2">
          <div className="flex items-center gap-0.5">
            {[1, 2, 3, 4, 5].map((i) => (
              <Star
                key={i}
                className={`w-3.5 h-3.5 ${
                  i <= Math.round(product.rating) ? "fill-amber-400 text-amber-400" : "text-slate-300"
                }`}
              />
            ))}
          </div>
          <span className="text-xs text-slate-500">
            {product.rating} · {product.review_count.toLocaleString("en-IN")}
          </span>
        </div>

        <div className="mt-3 font-store-heading font-bold text-lg text-slate-900">
          {formatINR(product.price_inr)}
        </div>
      </div>
    </Link>
  );
}

import { Link } from "react-router-dom";
import { Star } from "lucide-react";

function formatINR(n) {
  return "₹" + n.toLocaleString("en-IN");
}

// Compact Amazon-style product card — image, title, brand, price with MRP strike, rating
export default function ProductCard({ product }) {
  const mrp = Math.round(product.price_inr * 1.15);
  return (
    <Link
      to={`/product/${product.id}`}
      data-testid={`product-card-${product.id}`}
      className="group flex flex-col bg-white p-3 hover:shadow-lg hover:z-10 transition-shadow duration-200 rounded-md"
    >
      <div className="aspect-square rounded-md bg-white flex items-center justify-center overflow-hidden mb-3">
        <img
          src={product.image}
          alt={product.name}
          className="w-full h-full object-cover group-hover:scale-[1.03] transition-transform duration-500"
          loading="lazy"
        />
      </div>

      <div className="flex-1 flex flex-col">
        <div className="font-store-heading text-[13.5px] text-slate-900 leading-[1.35] line-clamp-2 min-h-[38px]">
          {product.name}
        </div>
        <div className="text-[12px] text-slate-500 mt-0.5">{product.brand}</div>

        <div className="mt-1.5 flex items-baseline gap-1.5">
          <span className="text-[11px] text-slate-400 align-top">₹</span>
          <span className="font-store-heading font-bold text-[18px] text-slate-900 leading-none">
            {product.price_inr.toLocaleString("en-IN")}
            <sup className="text-[10px] font-medium ml-0.5">00</sup>
          </span>
        </div>
        <div className="text-[11px] text-slate-500 mt-0.5">
          M.R.P: <span className="line-through">{formatINR(mrp)}</span>
        </div>

        <div className="mt-1.5 flex items-center gap-1">
          <div className="flex items-center gap-0.5">
            {[1, 2, 3, 4, 5].map((i) => (
              <Star
                key={i}
                className={`w-3 h-3 ${
                  i <= Math.round(product.rating) ? "fill-amber-400 text-amber-400" : "text-slate-300"
                }`}
              />
            ))}
          </div>
          <span className="text-[12px] text-slate-500">
            {product.review_count.toLocaleString("en-IN")}
          </span>
        </div>
      </div>
    </Link>
  );
}

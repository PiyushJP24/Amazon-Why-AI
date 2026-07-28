import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { fetchProduct } from "../lib/api";
import Header from "../components/Header";
import WhyAISidebar from "../components/WhyAISidebar";
import {
  Star,
  Truck,
  Shield,
  RotateCcw,
  ChevronRight,
  Sparkles,
  Check,
  Award,
  RefreshCw,
  CreditCard,
  Wallet,
  Building2,
  Gift,
  MapPin,
  ChevronLeft,
} from "lucide-react";

function formatINR(n) {
  return "₹" + n.toLocaleString("en-IN");
}

const OFFERS = [
  { icon: Wallet, title: "No Cost EMI", detail: "Upto ₹5,684 EMI interest savings on select Credit Cards", cta: "2 offers" },
  { icon: Gift, title: "Cashback", detail: "Upto ₹3,569 cashback as Amazon Pay Balance when using ICICI", cta: "1 offer" },
  { icon: Building2, title: "Bank Offer", detail: "Upto ₹3,000 discount on HSBC Bank Credit Cards", cta: "2 offers" },
  { icon: CreditCard, title: "Partner Offers", detail: "Get GST invoice and save up to 18% on business purchases", cta: "1 offer" },
];

const BADGES = [
  { icon: RefreshCw, label: "10 days Service", sub: "Centre Replacement" },
  { icon: Truck, label: "Free Delivery" },
  { icon: Shield, label: "1 Year", sub: "Warranty" },
  { icon: Wallet, label: "Pay on Delivery" },
  { icon: Award, label: "Top Brand" },
  { icon: Truck, label: "Amazon", sub: "Delivered" },
];

export default function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedThumb, setSelectedThumb] = useState(0);

  useEffect(() => {
    setLoading(true);
    fetchProduct(id)
      .then((p) => setProduct(p))
      .catch(() => setProduct(null))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50">
        <Header />
        <div className="max-w-[1500px] mx-auto px-4 py-8 grid md:grid-cols-3 gap-6">
          <div className="aspect-square bg-white rounded-md animate-pulse" />
          <div className="space-y-3">
            <div className="h-6 bg-white rounded w-2/3 animate-pulse" />
            <div className="h-4 bg-white rounded w-1/2 animate-pulse" />
            <div className="h-10 bg-white rounded w-1/3 animate-pulse" />
          </div>
          <div className="h-64 bg-white rounded-md animate-pulse" />
        </div>
      </div>
    );
  }
  if (!product) {
    return (
      <div className="min-h-screen bg-slate-50">
        <Header />
        <div className="max-w-4xl mx-auto p-10 text-center bg-white rounded-md mt-6">
          <div className="font-store-heading text-2xl font-bold">Product not found</div>
          <Link to="/" className="text-indigo-600 mt-4 inline-block">← Back to Amazon.in</Link>
        </div>
      </div>
    );
  }

  const mrp = Math.round(product.price_inr * 1.15);
  const discountPct = Math.round(((mrp - product.price_inr) / mrp) * 100);
  const stars = Math.round(product.rating);
  const mainImg = product.image;

  return (
    <div className="min-h-screen bg-slate-50">
      <Header />

      {/* Breadcrumb */}
      <div className="max-w-[1500px] mx-auto px-4 md:px-5 py-2 text-[12px] text-slate-500 flex items-center gap-1.5 flex-wrap">
        <Link to="/" className="hover:text-indigo-600">Electronics</Link>
        <ChevronRight className="w-3 h-3" />
        <Link to="/" className="hover:text-indigo-600">The AI Lab</Link>
        <ChevronRight className="w-3 h-3" />
        <span>{product.category}</span>
        <ChevronRight className="w-3 h-3" />
        <span className="text-slate-800 line-clamp-1 truncate">{product.name}</span>
      </div>

      {/* Main grid: reserve right space for WhyAI sidebar tab */}
      <div className="max-w-[1500px] mx-auto px-4 md:px-5 pb-16 md:pr-[440px]">
        <div className="bg-white rounded-md p-3 md:p-5 grid grid-cols-1 md:grid-cols-[80px_minmax(280px,1fr)_minmax(280px,1.05fr)_minmax(240px,280px)] gap-3 md:gap-5">
          {/* Column 1: Thumbnail strip */}
          <div className="hidden md:flex flex-col gap-2">
            {[0, 1, 2, 3, 4].map((i) => (
              <button
                key={i}
                onClick={() => setSelectedThumb(i)}
                data-testid={`thumb-${i}`}
                className={`w-16 h-16 rounded-md overflow-hidden ring-1 transition-all ${
                  selectedThumb === i ? "ring-2 ring-orange-500" : "ring-slate-200 hover:ring-slate-400"
                }`}
              >
                <img src={mainImg} alt="" className="w-full h-full object-cover" />
              </button>
            ))}
            <div className="w-16 h-16 rounded-md ring-1 ring-slate-200 flex items-center justify-center text-[10px] font-semibold text-slate-500">
              10+
            </div>
          </div>

          {/* Column 2: Main image */}
          <div className="min-w-0">
            <div className="aspect-square rounded-md bg-white border border-slate-100 overflow-hidden flex items-center justify-center">
              <img
                src={mainImg}
                alt={product.name}
                data-testid="product-main-image"
                className="w-full h-full object-cover"
              />
            </div>
            <div className="mt-3 md:hidden flex gap-2 overflow-x-auto no-scrollbar">
              {[0, 1, 2, 3].map((i) => (
                <button
                  key={i}
                  className="w-14 h-14 shrink-0 rounded-md overflow-hidden ring-1 ring-slate-200"
                >
                  <img src={mainImg} alt="" className="w-full h-full object-cover" />
                </button>
              ))}
            </div>
            <div className="mt-4 flex items-center justify-center gap-1 text-xs text-indigo-700">
              <button className="hover:underline">← See all photos</button>
              <span className="text-slate-300 mx-1">·</span>
              <button className="hover:underline">Click to see full view</button>
            </div>
          </div>

          {/* Column 3: Info */}
          <div className="min-w-0">
            <h1
              className="font-store-heading text-[22px] md:text-[24px] leading-tight font-medium text-slate-900"
              data-testid="product-title"
            >
              {product.name}
            </h1>
            <div className="mt-1.5 text-sm">
              <span className="text-slate-500">Visit the </span>
              <Link to="/" className="text-indigo-700 hover:text-orange-600 hover:underline">
                {product.brand} Store
              </Link>
            </div>

            {/* Rating */}
            <div className="mt-1.5 flex items-center gap-2 text-sm">
              <span className="font-semibold text-slate-900">{product.rating}</span>
              <div className="flex items-center gap-0.5">
                {[1, 2, 3, 4, 5].map((i) => (
                  <Star
                    key={i}
                    className={`w-3.5 h-3.5 ${
                      i <= stars ? "fill-amber-400 text-amber-400" : "text-slate-300"
                    }`}
                  />
                ))}
              </div>
              <Link to="/" className="text-indigo-700 hover:text-orange-600 hover:underline">
                ({product.review_count.toLocaleString("en-IN")})
              </Link>
            </div>
            <div className="mt-1 text-[13px] text-slate-700">
              <span className="font-semibold">5K+ bought</span> in past month
            </div>

            <hr className="my-3 border-slate-100" />

            {/* Price */}
            <div>
              <div className="flex items-baseline gap-2">
                <span className="text-red-600 text-lg font-medium">-{discountPct}%</span>
                <span className="font-store-heading text-[28px] leading-none text-slate-900">
                  <span className="text-[16px] align-top">₹</span>
                  <span className="font-semibold">{product.price_inr.toLocaleString("en-IN")}</span>
                </span>
              </div>
              <div className="mt-1 text-[13px] text-slate-500">
                M.R.P.: <span className="line-through">{formatINR(mrp)}</span>
              </div>
              <div className="text-[13px] text-slate-500">Inclusive of all taxes</div>
              <div className="mt-1.5 text-[13px] text-slate-700">
                <span className="font-semibold">EMI</span> starts at ₹{Math.round(product.price_inr / 24).toLocaleString("en-IN")}.
                No Cost EMI available.{" "}
                <Link to="/" className="text-indigo-700 hover:text-orange-600 hover:underline">EMI options ▾</Link>
              </div>
            </div>

            <hr className="my-3 border-slate-100" />

            {/* Offers */}
            <div>
              <div className="flex items-center gap-1.5 mb-2">
                <div className="w-6 h-6 rounded-full border border-slate-300 flex items-center justify-center">
                  <span className="text-xs font-bold text-slate-600">%</span>
                </div>
                <span className="font-semibold text-slate-900">Offers</span>
              </div>
              <div className="grid grid-cols-2 lg:grid-cols-4 gap-2">
                {OFFERS.map((o) => {
                  const I = o.icon;
                  return (
                    <div key={o.title} className="rounded-md border border-slate-200 p-2.5 text-[12px]">
                      <div className="flex items-center gap-1.5 font-semibold text-slate-900 mb-1">
                        <I className="w-3.5 h-3.5 text-slate-600" /> {o.title}
                      </div>
                      <div className="text-slate-700 leading-tight line-clamp-3">{o.detail}</div>
                      <button className="mt-1 text-indigo-700 hover:text-orange-600 hover:underline text-[12px]">
                        {o.cta} ›
                      </button>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Badges strip */}
            <div className="mt-4 flex items-start gap-3 overflow-x-auto no-scrollbar pb-2">
              {BADGES.map((b) => {
                const I = b.icon;
                return (
                  <div key={b.label} className="shrink-0 flex flex-col items-center gap-1 w-16 text-center">
                    <div className="w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center">
                      <I className="w-4 h-4 text-slate-600" />
                    </div>
                    <div className="text-[11px] text-indigo-700 leading-tight">
                      {b.label}
                      {b.sub && <div className="text-indigo-700">{b.sub}</div>}
                    </div>
                  </div>
                );
              })}
            </div>

            <hr className="my-3 border-slate-100" />

            {/* Colour swatches (visual only) */}
            <div className="mt-2">
              <div className="text-[13px] text-slate-700"><span className="font-semibold">Colour:</span> Titanium Black</div>
              <div className="mt-2 flex items-center gap-2">
                {[0, 1, 2, 3].map((i) => (
                  <div
                    key={i}
                    className={`rounded-md p-1 ring-1 ${
                      i === 0 ? "ring-orange-500" : "ring-slate-200 hover:ring-slate-400"
                    } cursor-pointer`}
                  >
                    <div className="w-14 h-14 rounded overflow-hidden">
                      <img src={mainImg} alt="" className="w-full h-full object-cover" />
                    </div>
                    <div className="text-[10px] text-center mt-1 text-slate-700 font-semibold">
                      ₹{product.price_inr.toLocaleString("en-IN")}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Spec table */}
            <div className="mt-4">
              <table className="w-full text-[13px]">
                <tbody>
                  <tr>
                    <td className="py-1.5 text-slate-500 w-1/3">Brand</td>
                    <td className="py-1.5 text-slate-900 font-medium">{product.brand}</td>
                  </tr>
                  <tr>
                    <td className="py-1.5 text-slate-500">Category</td>
                    <td className="py-1.5 text-slate-900 font-medium">{product.category}</td>
                  </tr>
                  <tr>
                    <td className="py-1.5 text-slate-500">Model</td>
                    <td className="py-1.5 text-slate-900 font-medium">{product.tagline}</td>
                  </tr>
                  <tr>
                    <td className="py-1.5 text-slate-500">Warranty</td>
                    <td className="py-1.5 text-slate-900 font-medium">1 Year Manufacturer</td>
                  </tr>
                </tbody>
              </table>
            </div>

            {/* About this item */}
            <div className="mt-4">
              <div className="font-store-heading text-lg font-bold text-slate-900 mb-2">About this item</div>
              <ul className="space-y-2" data-testid="feature-bullets">
                {product.features.map((f, i) => (
                  <li key={i} className="flex gap-2 text-[13.5px] leading-snug text-slate-800">
                    <span className="mt-1.5 w-1 h-1 rounded-full bg-slate-500 shrink-0" />
                    <span>
                      <span className="font-semibold text-slate-900">{f.feature_name} — </span>
                      <span>{f.technical_meaning}</span>
                    </span>
                  </li>
                ))}
              </ul>
              <div className="mt-3 rounded-md border border-indigo-100 bg-indigo-50/60 p-2.5 text-[13px] text-slate-700 flex items-start gap-2">
                <Sparkles className="w-4 h-4 text-indigo-500 mt-0.5 shrink-0" />
                <span>
                  <span className="font-whyai font-semibold text-indigo-700">Want this in plain English for you?</span>{" "}
                  Open the <span className="font-semibold">WhyAI</span> panel on the right — one sentence about how you'll use this, and every feature above becomes personal.
                </span>
              </div>
            </div>

            {/* Customers usually keep this item */}
            <div className="mt-4 rounded-md border-2 border-emerald-600 p-3 bg-white flex items-start gap-2.5">
              <div className="w-7 h-7 rounded-full bg-emerald-600 flex items-center justify-center shrink-0">
                <Check className="w-4 h-4 text-white" strokeWidth={3} />
              </div>
              <div>
                <div className="font-semibold text-slate-900">Customers usually keep this item</div>
                <div className="text-[13px] text-slate-600">
                  This product has fewer returns than average compared to similar products.
                </div>
              </div>
            </div>
          </div>

          {/* Column 4: Buy box (right sidebar) */}
          <div className="min-w-0 space-y-3">
            {/* Prime perk box */}
            <div className="rounded-md border border-slate-200 bg-slate-50 p-3">
              <div className="text-[11px] font-bold text-indigo-800 tracking-widest">prime</div>
              <div className="mt-1 text-[13px] text-slate-800 leading-snug">
                Enjoy <span className="font-semibold">Unlimited FREE Same day/1-day delivery</span>, Prime offers everyday and more
              </div>
              <button className="mt-2 text-indigo-700 hover:text-orange-600 hover:underline text-[13px] font-medium">
                Join Prime »
              </button>
            </div>

            {/* Buy box */}
            <div className="rounded-md border border-slate-200 bg-white p-3.5">
              <div className="text-[22px] font-store-heading text-slate-900">
                <span className="text-[13px] align-top">₹</span>
                <span className="font-semibold">{product.price_inr.toLocaleString("en-IN")}</span>
                <span className="text-[13px] font-normal ml-1">
                  <span className="line-through text-slate-500">{formatINR(mrp)}</span>
                </span>
              </div>
              <div className="mt-2 text-[13px] text-slate-800">
                FREE delivery <span className="font-semibold">Monday, 2 March</span>. Order within{" "}
                <span className="text-emerald-700 font-semibold">6 hrs 49 mins</span>{" "}
                <Link to="/" className="text-indigo-700 hover:underline">Details</Link>
              </div>
              <div className="mt-2 flex items-start gap-1 text-[13px] text-slate-800">
                <MapPin className="w-3.5 h-3.5 text-slate-500 mt-0.5 shrink-0" />
                <div>
                  <span>Delivering to Bengaluru 560001 - </span>
                  <Link to="/" className="text-indigo-700 hover:underline">Update location</Link>
                </div>
              </div>
              <div className="mt-3 text-emerald-700 text-lg font-semibold">In stock</div>
              <button
                data-testid="add-to-cart"
                className="mt-3 w-full rounded-full py-2.5 bg-amber-400 hover:bg-amber-500 text-slate-900 font-semibold text-[13px] active:scale-[0.99] transition-[transform,background-color]"
              >
                Add to Cart
              </button>
              <button
                data-testid="buy-now"
                className="mt-2 w-full rounded-full py-2.5 bg-orange-500 hover:bg-orange-600 text-white font-semibold text-[13px] active:scale-[0.99] transition-[transform,background-color]"
              >
                Buy Now
              </button>

              <div className="mt-4 text-[13px] space-y-1.5">
                <div className="flex justify-between"><span className="text-slate-500">Ships from</span><span className="text-slate-900">Amazon</span></div>
                <div className="flex justify-between"><span className="text-slate-500">Sold by</span><span className="text-slate-900">Clicktech Retail</span></div>
                <div className="flex justify-between"><span className="text-slate-500">Payment</span><span className="text-slate-900">Secure transaction</span></div>
                <div className="flex justify-between"><span className="text-slate-500">Gift options</span><Link to="/" className="text-indigo-700 hover:underline">Available at checkout</Link></div>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-100">
                <div className="text-[13px] font-semibold text-slate-900">Add a Protection Plan:</div>
                <label className="flex items-start gap-1.5 mt-2 text-[13px] cursor-pointer">
                  <input type="checkbox" className="mt-0.5" />
                  <span>1 Year Extended Warranty by Xtracover for <span className="font-semibold">₹6,229.00</span></span>
                </label>
                <label className="flex items-start gap-1.5 mt-1.5 text-[13px] cursor-pointer">
                  <input type="checkbox" className="mt-0.5" />
                  <span>1 Year Screen Protection by Acko for <span className="font-semibold">₹3,799.00</span></span>
                </label>
              </div>

              <button className="mt-4 w-full rounded-full py-2 border border-slate-300 text-slate-800 text-[13px] font-medium hover:bg-slate-50 transition-colors">
                Add to Wish List
              </button>
            </div>
          </div>
        </div>
      </div>

      <WhyAISidebar product={product} />
    </div>
  );
}

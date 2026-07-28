import { Smartphone, Laptop, Tv, Watch, Glasses, WashingMachine } from "lucide-react";

// Circular "Amazon AI Tech Lab" style category tile — icon on a purple podium
const ICONS = {
  Smartphones: Smartphone,
  Laptops: Laptop,
  Televisions: Tv,
  Smartwatches: Watch,
  "Smart Glasses": Glasses,
  "Home Appliances": WashingMachine,
};

export default function CategoryTile({ category, onClick, active }) {
  const Icon = ICONS[category] || Smartphone;
  return (
    <button
      onClick={onClick}
      data-testid={`cat-tile-${category}`}
      className={`group flex flex-col items-center gap-2 transition-transform duration-200 hover:-translate-y-1 active:scale-[0.98] ${
        active ? "" : ""
      }`}
    >
      <div className="relative">
        <div className="absolute inset-x-2 -bottom-1 h-3 rounded-[50%] bg-indigo-900/25 blur-[3px]" />
        <div
          className={`relative w-24 h-24 sm:w-28 sm:h-28 rounded-full flex items-center justify-center shadow-md ${
            active
              ? "bg-gradient-to-br from-indigo-100 to-white ring-2 ring-indigo-400"
              : "bg-gradient-to-br from-slate-100 to-white ring-1 ring-slate-200 group-hover:ring-indigo-300"
          } transition-shadow`}
        >
          <div
            className={`w-14 h-14 rounded-full flex items-center justify-center ${
              active ? "bg-gradient-to-br from-indigo-500 to-cyan-400" : "bg-gradient-to-br from-slate-700 to-slate-900"
            } transition-colors`}
          >
            <Icon className="w-7 h-7 text-white" strokeWidth={1.6} />
          </div>
        </div>
      </div>
      <div className={`text-[13px] font-store-heading font-semibold ${active ? "text-indigo-600" : "text-slate-800"}`}>
        {category}
      </div>
    </button>
  );
}

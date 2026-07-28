import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { toast } from "sonner";
import {
  Sparkles,
  X,
  ArrowRight,
  ChevronDown,
  ChevronUp,
  ThumbsUp,
  ThumbsDown,
  Loader2,
  Pencil,
} from "lucide-react";
import { useUseCase } from "../context/UseCaseContext";
import { whyaiGenerate, whyaiTellMore, whyaiFeedback } from "../lib/api";

const LOADING_STEPS = [
  "Understanding your use case…",
  "Matching it to real specs…",
  "Checking what similar buyers say…",
];

const PLACEHOLDER_ROTATION_BY_CATEGORY = {
  Smartphones: [
    "I edit videos for my YouTube channel on weekends",
    "I mostly use my phone for work calls and email",
    "I game a lot on my phone during commutes",
    "I click a lot of family photos and travel photos",
  ],
  Laptops: [
    "I edit video content and stream on Twitch",
    "I take a lot of client calls from home",
    "I'm a student — mostly notes, PDFs, and coding",
    "I do photo editing in Lightroom on weekends",
  ],
  Televisions: [
    "We watch a lot of movies and cricket with the family",
    "I use it for PS5 gaming most weekends",
    "Mostly Netflix and old family videos",
  ],
  Smartwatches: [
    "I run and lift 4x a week and track everything",
    "I want to keep an eye on my parents' health signals",
    "I sit at a desk all day — I need move reminders",
  ],
  "Smart Glasses": [
    "I travel a lot and don't speak local languages",
    "I want hands-free POV clips for my content",
    "I take a lot of calls while walking",
  ],
  "Home Appliances": [
    "I run a family of five with heavy AC use",
    "I do meal-prep every Sunday for the week",
    "I do lots of small laundry loads in a small apartment",
  ],
};

function confidenceStyle(pct) {
  if (pct >= 80) {
    return {
      bg: "bg-emerald-50",
      text: "text-emerald-800",
      border: "border-emerald-200",
      dot: "bg-emerald-500",
      label: "🟢",
    };
  }
  if (pct >= 60) {
    return {
      bg: "bg-amber-50",
      text: "text-amber-800",
      border: "border-amber-200",
      dot: "bg-amber-500",
      label: "🟡",
    };
  }
  return {
    bg: "bg-orange-50",
    text: "text-orange-800",
    border: "border-orange-200",
    dot: "bg-orange-500",
    label: "🟠",
  };
}

function RotatingPlaceholder({ options }) {
  const [i, setI] = useState(0);
  useEffect(() => {
    const t = setInterval(() => setI((n) => (n + 1) % options.length), 2600);
    return () => clearInterval(t);
  }, [options.length]);
  return <span className="text-slate-400">e.g. {options[i]}</span>;
}

function FeatureCard({ card, index, product, useCaseData, sessionId }) {
  const [open, setOpen] = useState(false);
  const [loadingMore, setLoadingMore] = useState(false);
  const [more, setMore] = useState("");
  const [feedback, setFeedback] = useState(null);
  const style = confidenceStyle(card.confidence_pct);

  const onTellMore = async () => {
    setOpen((o) => !o);
    if (!open && !more) {
      setLoadingMore(true);
      try {
        const res = await whyaiTellMore({
          use_case_text: useCaseData.raw,
          cluster: useCaseData.cluster,
          product_id: product.id,
          feature_name: card.feature_name,
        });
        setMore(res.explanation);
      } catch (e) {
        setMore("Sorry, couldn't fetch a deeper explanation right now.");
      } finally {
        setLoadingMore(false);
      }
    }
  };

  const onThumb = async (thumbs) => {
    setFeedback(thumbs);
    try {
      await whyaiFeedback({
        session_id: sessionId,
        product_id: product.id,
        feature_name: card.feature_name,
        thumbs,
      });
      toast.success(thumbs === "up" ? "Thanks — glad this helped!" : "Thanks — we'll keep learning.");
    } catch (e) {
      toast.error("Couldn't record feedback.");
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.08, type: "spring", damping: 18 }}
      className="rounded-2xl bg-white ring-1 ring-indigo-50 shadow-sm p-4"
      data-testid={`whyai-feature-card-${index}`}
    >
      <div className="text-[11px] font-semibold uppercase tracking-wider text-indigo-600">
        {card.feature_name}
      </div>
      <div className="mt-1.5 text-[15px] leading-snug text-slate-800 font-whyai">
        {card.personalized_benefit}
      </div>

      <div className={`mt-3 inline-flex items-start gap-2 px-2.5 py-1 rounded-full text-xs font-medium border ${style.bg} ${style.text} ${style.border}`}>
        <span className={`w-1.5 h-1.5 rounded-full ${style.dot} mt-1`} />
        <span>
          {card.confidence_scope === "feature+usecase" && (
            <>{card.confidence_pct}% of buyers with a similar use case rated this feature positively <span className="text-slate-400">· n={card.sample_size}</span></>
          )}
          {card.confidence_scope === "feature" && (
            <>{card.confidence_pct}% of buyers rated this feature positively <span className="text-slate-400">· n={card.sample_size}</span></>
          )}
          {card.confidence_scope === "product_overall" && (
            <>Based on overall product reviews — limited feature-specific data available <span className="text-slate-400">· {card.confidence_pct}% (n={card.sample_size})</span></>
          )}
        </span>
      </div>

      <div className="mt-3 flex items-center justify-between">
        <button
          data-testid={`tell-more-${index}`}
          onClick={onTellMore}
          className="text-[13px] font-medium text-indigo-600 hover:text-indigo-700 inline-flex items-center gap-1"
        >
          {open ? "Show less" : "Tell me more"}
          {open ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
        </button>
        <div className="flex items-center gap-1">
          <button
            data-testid={`thumb-up-${index}`}
            onClick={() => onThumb("up")}
            className={`p-1.5 rounded-full transition-colors ${
              feedback === "up" ? "bg-emerald-100 text-emerald-700" : "text-slate-400 hover:bg-slate-100 hover:text-slate-700"
            }`}
            aria-label="Thumbs up"
          >
            <ThumbsUp className="w-3.5 h-3.5" />
          </button>
          <button
            data-testid={`thumb-down-${index}`}
            onClick={() => onThumb("down")}
            className={`p-1.5 rounded-full transition-colors ${
              feedback === "down" ? "bg-rose-100 text-rose-700" : "text-slate-400 hover:bg-slate-100 hover:text-slate-700"
            }`}
            aria-label="Thumbs down"
          >
            <ThumbsDown className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="overflow-hidden"
          >
            <div className="mt-3 pt-3 border-t border-slate-100 text-[13.5px] leading-relaxed text-slate-700">
              {loadingMore ? (
                <div className="flex items-center gap-2 text-slate-500">
                  <Loader2 className="w-3.5 h-3.5 animate-spin" /> Thinking…
                </div>
              ) : (
                more
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}

export default function WhyAISidebar({ product }) {
  const { useCase, setUseCase, clear } = useUseCase();
  const [open, setOpen] = useState(false);
  const [inputText, setInputText] = useState("");
  const [loading, setLoading] = useState(false);
  const [loadingStep, setLoadingStep] = useState(0);
  const [result, setResult] = useState(null); // {session_id, use_case, cards}
  const [editing, setEditing] = useState(false);

  const placeholders =
    PLACEHOLDER_ROTATION_BY_CATEGORY[product.category] ||
    PLACEHOLDER_ROTATION_BY_CATEGORY["Smartphones"];

  // Auto-run if we already have a use case from another product
  useEffect(() => {
    if (useCase?.text && open && !result && !loading) {
      runGenerate(useCase.text);
    }
    // eslint-disable-next-line
  }, [open, product.id]);

  // Loading step animation
  useEffect(() => {
    if (!loading) return;
    setLoadingStep(0);
    const t1 = setTimeout(() => setLoadingStep(1), 900);
    const t2 = setTimeout(() => setLoadingStep(2), 1900);
    return () => {
      clearTimeout(t1);
      clearTimeout(t2);
    };
  }, [loading]);

  const runGenerate = async (text) => {
    setLoading(true);
    setResult(null);
    try {
      const res = await whyaiGenerate({
        use_case_text: text,
        product_id: product.id,
      });
      setResult(res);
      setUseCase({ text, cluster: res.use_case.cluster });
    } catch (e) {
      const status = e?.response?.status;
      const msg = status === 429
        ? "AI service is busy right now — try again in a minute."
        : "Couldn't generate WhyAI insights. Try again.";
      toast.error(msg);
    } finally {
      setLoading(false);
    }
  };

  const onSubmit = (e) => {
    e.preventDefault();
    const text = inputText.trim();
    if (!text) return;
    setEditing(false);
    runGenerate(text);
  };

  const onChangeUseCase = () => {
    setEditing(true);
    setResult(null);
    setInputText(useCase?.text || "");
  };

  return (
    <>
      {/* Collapsed tab */}
      <AnimatePresence>
        {!open && (
          <motion.button
            key="whyai-tab"
            data-testid="whyai-tab"
            onClick={() => setOpen(true)}
            initial={{ opacity: 0, x: 30 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: 30 }}
            className="whyai-pulse fixed right-0 top-1/2 -translate-y-1/2 z-40 rounded-l-2xl px-3.5 py-4 text-white bg-gradient-to-b from-indigo-500 to-cyan-500 flex items-center gap-2 font-whyai text-sm font-semibold hover:from-indigo-600 hover:to-cyan-600 transition-colors"
            style={{ writingMode: "horizontal-tb" }}
          >
            <Sparkles className="w-4 h-4" />
            <span className="hidden sm:inline">WhyAI — see what this means for you</span>
            <span className="sm:hidden">WhyAI</span>
            <ArrowRight className="w-4 h-4" />
          </motion.button>
        )}
      </AnimatePresence>

      {/* Panel */}
      <AnimatePresence>
        {open && (
          <motion.div
            key="whyai-panel"
            initial={{ x: "100%" }}
            animate={{ x: 0 }}
            exit={{ x: "100%" }}
            transition={{ type: "spring", damping: 26, stiffness: 220 }}
            className="fixed right-0 top-0 h-screen w-full sm:w-[420px] z-50 flex flex-col bg-white/95 backdrop-blur-2xl shadow-[-10px_0_30px_rgba(0,0,0,0.06)] border-l border-indigo-100"
            data-testid="whyai-panel"
          >
            {/* Header */}
            <div className="px-5 py-4 border-b border-slate-100 flex items-center justify-between shrink-0">
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-indigo-500 to-cyan-400 flex items-center justify-center">
                  <Sparkles className="w-4 h-4 text-white" strokeWidth={2.4} />
                </div>
                <div>
                  <div className="font-whyai font-bold text-slate-900 leading-none">WhyAI</div>
                  <div className="text-[11px] text-slate-500 leading-none mt-0.5">Personalized feature translator</div>
                </div>
              </div>
              <button
                onClick={() => setOpen(false)}
                data-testid="whyai-close"
                className="p-1.5 rounded-full text-slate-500 hover:bg-slate-100 hover:text-slate-800 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* Persistent use-case chip */}
            {useCase?.text && !editing && (
              <div className="px-5 py-3 border-b border-slate-100 shrink-0">
                <div className="flex items-start gap-2 rounded-xl bg-indigo-50 text-indigo-800 px-3 py-2 text-[13px] border border-indigo-100">
                  <div className="flex-1">
                    <span className="text-indigo-500 font-medium">Using:</span>{" "}
                    <span className="font-whyai">{useCase.text}</span>
                  </div>
                  <button
                    onClick={onChangeUseCase}
                    data-testid="whyai-change-usecase"
                    className="text-indigo-600 hover:text-indigo-800 flex items-center gap-0.5 shrink-0"
                  >
                    <Pencil className="w-3 h-3" /> change
                  </button>
                </div>
              </div>
            )}

            <div className="flex-1 overflow-y-auto no-scrollbar px-5 py-4">
              {/* Input state */}
              {(!useCase?.text || editing) && !loading && !result && (
                <form onSubmit={onSubmit} className="whyai-fadeup">
                  <div className="font-whyai text-[22px] font-semibold text-slate-900 leading-tight">
                    How will you mainly use this?
                  </div>
                  <p className="text-[13px] text-slate-500 mt-1.5 leading-relaxed">
                    Just one sentence. WhyAI will translate every AI feature into what it means <em>for you</em>.
                  </p>

                  <div className="mt-4 rounded-2xl border border-slate-200 focus-within:border-indigo-300 focus-within:ring-2 focus-within:ring-indigo-100 bg-white p-3 transition-colors">
                    <textarea
                      data-testid="whyai-usecase-input"
                      value={inputText}
                      onChange={(e) => setInputText(e.target.value)}
                      rows={3}
                      className="w-full bg-transparent outline-none text-[14px] font-whyai resize-none placeholder:text-slate-400"
                      placeholder=""
                    />
                    {!inputText && (
                      <div className="text-[13px] pointer-events-none -mt-8 px-1">
                        <RotatingPlaceholder options={placeholders} />
                      </div>
                    )}
                  </div>

                  <button
                    type="submit"
                    data-testid="whyai-submit"
                    disabled={!inputText.trim()}
                    className="mt-4 w-full rounded-full py-2.5 bg-gradient-to-r from-indigo-500 to-cyan-500 text-white font-whyai font-semibold text-sm hover:opacity-95 active:scale-[0.99] transition-[opacity,transform] disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    Show me what this means →
                  </button>
                </form>
              )}

              {/* Loading state */}
              {loading && (
                <div className="whyai-fadeup" aria-live="polite">
                  <div className="font-whyai text-[18px] font-semibold text-slate-900">
                    Working on it…
                  </div>
                  <ol className="mt-4 space-y-3">
                    {LOADING_STEPS.map((s, i) => (
                      <li key={i} className="flex items-center gap-3 text-[13.5px]">
                        <div
                          className={`w-5 h-5 rounded-full flex items-center justify-center shrink-0 ${
                            i < loadingStep
                              ? "bg-emerald-500 text-white"
                              : i === loadingStep
                              ? "bg-gradient-to-tr from-indigo-500 to-cyan-500 text-white"
                              : "bg-slate-200 text-slate-500"
                          }`}
                        >
                          {i < loadingStep ? (
                            <svg className="w-3 h-3" viewBox="0 0 20 20" fill="currentColor">
                              <path d="M16.7 5.3l-8.4 8.4-4-4-1.4 1.4 5.4 5.4 9.8-9.8z" />
                            </svg>
                          ) : i === loadingStep ? (
                            <Loader2 className="w-3 h-3 animate-spin" />
                          ) : (
                            <span className="text-[10px]">{i + 1}</span>
                          )}
                        </div>
                        <span className={i <= loadingStep ? "text-slate-900" : "text-slate-500"}>{s}</span>
                      </li>
                    ))}
                  </ol>
                </div>
              )}

              {/* Results state */}
              {result && !loading && (
                <div className="space-y-3">
                  {result.cards.map((c, i) => (
                    <FeatureCard
                      key={i}
                      index={i}
                      card={c}
                      product={product}
                      useCaseData={result.use_case}
                      sessionId={result.session_id}
                    />
                  ))}
        <div className="pt-2 pb-6 text-center text-[11px] text-slate-400 font-whyai">
          Grounded in this product's specs · per-feature two-layer RAG
        </div>
                </div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}

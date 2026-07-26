import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Toaster } from "@/components/ui/sonner";
import Home from "@/pages/Home";
import ProductDetail from "@/pages/ProductDetail";
import { UseCaseProvider } from "@/context/UseCaseContext";

function App() {
  return (
    <div className="App">
      <UseCaseProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/product/:id" element={<ProductDetail />} />
          </Routes>
        </BrowserRouter>
        <Toaster position="top-center" richColors />
      </UseCaseProvider>
    </div>
  );
}

export default App;

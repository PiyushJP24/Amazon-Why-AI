import React, { createContext, useContext, useEffect, useState } from "react";

const KEY = "whyai_use_case_v1";

const UseCaseContext = createContext(null);

export function UseCaseProvider({ children }) {
  const [useCase, setUseCaseState] = useState(() => {
    try {
      const raw = sessionStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  });

  useEffect(() => {
    try {
      if (useCase) sessionStorage.setItem(KEY, JSON.stringify(useCase));
      else sessionStorage.removeItem(KEY);
    } catch {}
  }, [useCase]);

  const setUseCase = (payload) => setUseCaseState(payload);
  const clear = () => setUseCaseState(null);

  return (
    <UseCaseContext.Provider value={{ useCase, setUseCase, clear }}>
      {children}
    </UseCaseContext.Provider>
  );
}

export const useUseCase = () => useContext(UseCaseContext);

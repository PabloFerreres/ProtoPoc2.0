
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// Suppress ResizeObserver loop limit exceeded warning
window.addEventListener("error", (e) => {
  if (e.message && e.message.includes("ResizeObserver loop limit exceeded")) {
    e.stopImmediatePropagation();
  }
});

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

import React, { useState } from "react";
import AgGridTable from "./AgGridTable";
import MasterTable from "./MasterTable";

function App() {
  const [view, setView] = useState("project");

  return (
    <div>
      <h1>ProtoPoC – Tabellenansicht</h1>
      <div style={{ marginBottom: "16px" }}>
        <button onClick={() => setView("project")} style={{ marginRight: 8 }}>
          📋 Projektliste
        </button>
        <button onClick={() => setView("master")}>
          🧱 Mastertabelle
        </button>
      </div>

      {view === "project" && <AgGridTable />}
      {view === "master" && <MasterTable />}
    </div>
  );
}

export default App;
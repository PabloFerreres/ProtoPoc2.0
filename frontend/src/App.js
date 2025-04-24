import React, { useState, useEffect } from "react";
import axios from "axios";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";

function App() {
  const [projects, setProjects] = useState([]);
  const [selected, setSelected] = useState("");
  const [rowData, setRowData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/projects").then(res => setProjects(res.data));
  }, []);

  useEffect(() => {
    if (selected)
      axios.get(`http://localhost:8000/project/${selected}`).then(res => setRowData(res.data));
  }, [selected]);

  return (
    <div className="ag-theme-alpine" style={{ height: 600 }}>
      <h2>Projekt-Auswahl</h2>
      <select onChange={(e) => setSelected(e.target.value)} value={selected}>
        <option value="">Projekt wählen</option>
        {projects.map(p => (
          <option key={p} value={p}>{p}</option>
        ))}
      </select>
      <AgGridReact rowData={rowData} columnDefs={rowData[0] ? Object.keys(rowData[0]).map(k => ({ field: k })) : []} />
    </div>
  );
}

export default App;
import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";
import "./AgGridColors.css";

const AgGridTable = () => {
  const [projects, setProjects] = useState([]);
  const [selected, setSelected] = useState("");
  const [rowData, setRowData] = useState([]);
  const [columnDefs, setColumnDefs] = useState([]);
  const gridRef = useRef();

  useEffect(() => {
    axios.get("http://localhost:8000/projects").then((res) => setProjects(res.data));
  }, []);

  useEffect(() => {
    if (selected) {
      axios.get(`http://localhost:8000/project/${selected}`).then((res) => {
        const data = res.data;
        setRowData(data);
        if (data.length > 0) {
          const keys = Object.keys(data[0]);
          const editableFields = ["Bauteil", "Beschreibung", "Revision"];
          setColumnDefs(
            keys.map((key) => ({
              field: key,
              headerClass: `header-${key.replace(/ /g, "_")}`,
              editable: editableFields.includes(key)
            }))
          );
        }
      });
    }
  }, [selected]);

  const handleSave = () => {
    if (!gridRef.current) return;
    const updatedRows = gridRef.current.api.getDisplayedRowCount();
    for (let i = 0; i < updatedRows; i++) {
      const rowNode = gridRef.current.api.getDisplayedRowAtIndex(i);
      const data = rowNode.data;
      axios.post("http://localhost:8000/update_row", data).then((res) => {
        console.log("Gespeichert:", res.data);
      });
    }
    alert("Änderungen gespeichert.");
  };

  return (
    <div>
      <h2>Projekt auswählen</h2>
      <select onChange={(e) => setSelected(e.target.value)} value={selected}>
        <option value="">-- wählen --</option>
        {projects.map((p) => (
          <option key={p} value={p}>{p}</option>
        ))}
      </select>
      <div className="ag-theme-alpine" style={{ height: 600, marginTop: 20 }}>
        <AgGridReact
          ref={gridRef}
          rowData={rowData}
          columnDefs={columnDefs}
          defaultColDef={{ resizable: true, sortable: true }}
        />
      </div>
      <button onClick={handleSave} style={{ marginTop: 16 }}>💾 Änderungen speichern</button>
    </div>
  );
};

export default AgGridTable;
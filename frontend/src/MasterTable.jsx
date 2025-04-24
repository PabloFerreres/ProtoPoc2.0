import React, { useEffect, useState, useRef } from "react";
import axios from "axios";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";

const MasterTable = () => {
  const [rowData, setRowData] = useState([]);
  const gridRef = useRef();

  useEffect(() => {
    axios.get("http://localhost:8000/master").then((res) => {
      setRowData(res.data);
    });
  }, []);

  const columnDefs = rowData[0]
    ? Object.keys(rowData[0]).map((key) => {
        if (key === "Revision") {
          return { field: key, editable: false };
        }
        if (key === "Magische-Relevanz") {
          return {
            field: key,
            editable: true,
            cellEditor: "agSelectCellEditor",
            cellEditorParams: {
              values: ["", "M", "MS"]
            }
          };
        }
        return { field: key, editable: true };
      })
    : [];

  const handleSave = () => {
    if (!gridRef.current) return;
    const updatedRows = gridRef.current.api.getDisplayedRowCount();
    for (let i = 0; i < updatedRows; i++) {
      const rowNode = gridRef.current.api.getDisplayedRowAtIndex(i);
      const data = rowNode.data;
      axios.post("http://localhost:8000/update_master_row", data).then((res) => {
        console.log("Masterdatensatz gespeichert:", res.data);
      });
    }
    alert("Masterdaten gespeichert.");
  };

  return (
    <div className="ag-theme-alpine" style={{ height: 600 }}>
      <h2>Mastertabelle – Bauteile</h2>
      <AgGridReact
        ref={gridRef}
        rowData={rowData}
        columnDefs={columnDefs}
        defaultColDef={{ resizable: true, sortable: true, filter: true }}
      />
      <button onClick={handleSave} style={{ marginTop: 16 }}>💾 Änderungen speichern</button>
    </div>
  );
};

export default MasterTable;
import React, { useRef, useEffect } from "react";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";

const BaseTable = ({
  rowData,
  title,
  editableFields = [],
  nonEditableFields = [],
  zoom,
  setZoom,
  maxWidthMap = {}
}) => {
  const gridRef = useRef();

  const defaultColDef = {
    resizable: true,
    wrapText: true,
    autoHeight: true,
    sortable: true,
    filter: true,
    headerClass: "custom-header"
  };

  const headerColorMap = {
    "Call-ID": "#a64ca6",
    "Bauteil": "#66bb6a",
    "Ort": "#81d4fa",
    "Kommentar": "#ffd54f",
    "Lieferant": "#64b5f6",
    "Einbauort": "#e1bee7",
    "Magische-Relevanz": "#f06292",
    "Hersteller": "#4db6ac",
    "Material": "#ffcc80",
    "Spell": "#ce93d8",
    "Größe": "#90caf9",
    "Gewicht": "#a1887f",
    "Beschreibung": "#fff59d"
  };

  const columnDefs = rowData[0]
    ? Object.keys(rowData[0]).map((key) => ({
        field: key,
        editable:
          editableFields.includes(key) ||
          (!nonEditableFields.includes(key) && editableFields.length === 0),
        wrapText: true,
        autoHeight: true,
        sortable: true,
        filter: true,
        resizable: true,
        maxWidth: maxWidthMap[key] || 250,
        minWidth: 100,
        cellStyle: { whiteSpace: "normal", wordBreak: "break-word" },
        headerStyle: {
          backgroundColor: headerColorMap[key] || "#e0e0e0",
          fontWeight: "bold"
        }
      }))
    : [];

  const handleZoom = (direction) => {
    setZoom((prev) => {
      const newZoom = direction === "in" ? Math.min(prev + 0.1, 2.0) : Math.max(prev - 0.1, 0.5);
      return parseFloat(newZoom.toFixed(2));
    });
  };

  useEffect(() => {
    setTimeout(() => {
      if (gridRef.current && gridRef.current.api) {
        gridRef.current.api.sizeColumnsToFit();
      }
    }, 100);
  }, [rowData]);

  return (
    <div>
      <h2>{title}</h2>
      <div style={{ marginBottom: 10 }}>
        <button onClick={() => handleZoom("out")}>🔍– Zoom out</button>
        <button onClick={() => handleZoom("in")}>🔍+ Zoom in</button>
        <span style={{ marginLeft: 10 }}>Zoom: {Math.round(zoom * 100)}%</span>
      </div>
      <div
        className="ag-theme-alpine"
        style={{
          height: "80vh",
          width: `${100 / zoom}%`,
          transform: `scale(${zoom})`,
          transformOrigin: "top left",
          overflow: "auto"
        }}
      >
        <AgGridReact
          ref={gridRef}
          rowData={rowData}
          columnDefs={columnDefs}
          defaultColDef={defaultColDef}
          onGridReady={(params) => {
            if (gridRef.current && gridRef.current.api) {
              gridRef.current.api.sizeColumnsToFit();
            }
          }}
        />
      </div>
    </div>
  );
};

export default BaseTable;
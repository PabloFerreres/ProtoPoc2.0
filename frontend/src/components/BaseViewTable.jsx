import React from "react";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";  // Standard CSS für ag-Grid
import "ag-grid-community/styles/ag-theme-alpine.css"; // Alpine Theme für ag-Grid
import "./AgGridColors.css";  // Verwende den relativen Pfad
import axios from "axios";

const BaseViewTable = ({
  rowData = [],
  title = "Tabelle",
  zoom = 1.0,
  setZoom = () => {},
  columnDefs = [],
  gridRef,
  rowHeight,
  saveLayout,
}) => {
  const defaultColDef = {
    resizable: true,
    wrapText: true,
    autoHeight: true,
    sortable: true,
    filter: true,
  };

  const onGridReady = (params) => {
    params.api.sizeColumnsToFit();
  };

  return (
    <div style={{ position: "relative", transform: `scale(${zoom})`, transformOrigin: "top left" }}>
      <h2>{title}</h2>
      <div className="ag-theme-alpine" style={{ height: "80vh", width: "100%" }}>
        <AgGridReact
          ref={gridRef}
          rowData={rowData}
          columnDefs={columnDefs}
          defaultColDef={defaultColDef}
          onGridReady={onGridReady}
          rowHeight={rowHeight}  // Feste Zeilenhöhe anwenden
          onColumnResized={saveLayout}
          onColumnMoved={saveLayout}
        />
      </div>
    </div>
  );
};

export default BaseViewTable;

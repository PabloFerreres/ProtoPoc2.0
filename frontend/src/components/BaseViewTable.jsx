import React from "react";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";
import axios from "axios";
import "./AgGridColors.css";  // <-- wichtig!

const BaseViewTable = ({
  rowData = [],
  title = "Tabelle",
  zoom = 1.0,
  setZoom = () => {},
  columnDefs = [],
  gridRef,
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

  const saveLayout = () => {
    if (!gridRef.current || !gridRef.current.columnApi) return;

    const columnState = gridRef.current.columnApi.getColumnState();
    const layout = {
      columns: {},
      order: columnState.map((col) => col.colId),
    };

    columnState.forEach((col) => {
      layout.columns[col.colId] = { width: col.width };
    });

    axios.post("http://localhost:8000/save_layout", {
      projekt_id: "TestBauteile",
      view_type: "project",
      column_settings: layout,
    });
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
          onColumnResized={saveLayout}
          onColumnMoved={saveLayout}
        />
      </div>
    </div>
  );
};

export default BaseViewTable;

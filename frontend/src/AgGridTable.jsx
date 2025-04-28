import React, { useEffect, useState, useRef } from "react";
import axios from "axios";
import BaseTable from "./components/BaseTable";

const AgGridTable = () => {
  const [rowData, setRowData] = useState([]);
  const [zoom, setZoom] = useState(1.0);
  const [columnDefs, setColumnDefs] = useState([]);
  const gridRef = useRef();

  useEffect(() => {
    const loadDataAndLayout = async () => {
      const resData = await axios.get("http://localhost:8000/project/TestBauteile");
      setRowData(resData.data);

      if (resData.data.length > 0) {
        const fields = Object.keys(resData.data[0]);
        const defaultCols = fields.map((field, index) => ({
          field,
          headerClass: `header-group-${Math.floor(index / 5) + 1}`, // Jede 5. Spalte eine eigene Farbe
        }));
        setColumnDefs(defaultCols);
      }

      // Layout laden
      try {
        const resLayout = await axios.get("http://localhost:8000/layout/TestBauteile");
        const layout = resLayout.data;
        if (layout && layout.order && gridRef.current) {
          setTimeout(() => {
            gridRef.current.columnApi.applyColumnState({
              state: layout.order.map((colId) => ({
                colId,
                width: layout.columns[colId]?.width,
              })),
              applyOrder: true,
            });
          }, 300);
        }
      } catch (error) {
        console.error("Fehler beim Laden des Layouts:", error);
      }
    };

    loadDataAndLayout();
  }, []);

  const rowHeight = 40;  // Feste Zeilenhöhe

  const saveLayout = () => {
    if (!gridRef.current || !gridRef.current.columnApi) return;

    // Holen der Spalten-Konfiguration (Reihenfolge, Breite)
    const columnState = gridRef.current.columnApi.getColumnState();
    const layout = {
      columns: {},
      order: columnState.map((col) => col.colId),
    };

    // Speichern der Breiten der Spalten
    columnState.forEach((col) => {
      layout.columns[col.colId] = { width: col.width };
    });

    // Senden der Layout-Daten an das Backend
    axios.post("http://localhost:8000/save_layout", {
      projekt_id: "TestBauteile",
      view_type: "project",
      column_settings: layout,
    })
    .then(response => {
      console.log("Layout gespeichert:", response.data);
    })
    .catch(error => {
      console.error("Fehler beim Speichern des Layouts:", error);
    });
  };

  return (
    <div>
      <BaseTable
        title="TestBauteile Tabelle"
        rowData={rowData}
        zoom={zoom}
        setZoom={setZoom}
        columnDefs={columnDefs}
        gridRef={gridRef}
        rowHeight={rowHeight}  // Feste Zeilenhöhe
        saveLayout={saveLayout}  // Übergabe der saveLayout Funktion
      />
    </div>
  );
};

export default AgGridTable;

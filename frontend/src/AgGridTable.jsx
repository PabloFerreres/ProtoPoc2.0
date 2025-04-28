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
          headerClass: `header-group-${Math.floor(index / 5)}`, // Alle 5 Spalten gleiche Klasse
        }));
        setColumnDefs(defaultCols);

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
      }
    };

    loadDataAndLayout();
  }, []);

  return (
    <div>
      <BaseTable
        title="TestBauteile Tabelle"
        rowData={rowData}
        zoom={zoom}
        setZoom={setZoom}
        columnDefs={columnDefs}
        gridRef={gridRef}
      />
    </div>
  );
};

export default AgGridTable;

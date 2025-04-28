import React, { useEffect, useState } from "react";
import axios from "axios";
import BaseTable from "./components/BaseTable";

const AgGridTable = () => {
  const [rowData, setRowData] = useState([]);
  const [zoom, setZoom] = useState(1.0);
  const [columnDefs, setColumnDefs] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/project/TestBauteile").then((res) => {
      setRowData(res.data);

      if (res.data.length > 0) {
        const fields = Object.keys(res.data[0]);
        setColumnDefs(
          fields.map((field) => ({
            field,
            headerClass: `header-${field.replaceAll(/[^a-zA-Z0-9]/g, "_")}`,
          }))
        );
      }
    });
  }, []);

  return (
    <div>
      <BaseTable
        title="TestBauteile Tabelle"
        rowData={rowData}
        zoom={zoom}
        setZoom={setZoom}
        columnDefs={columnDefs}
      />
    </div>
  );
};

export default AgGridTable;

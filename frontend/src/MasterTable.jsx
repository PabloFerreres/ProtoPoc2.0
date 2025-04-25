import React, { useEffect, useState } from "react";
import axios from "axios";
import BaseTable from "./components/BaseTable";

const MasterTable = () => {
  const [rowData, setRowData] = useState([]);
  const [zoom, setZoom] = useState(1.0);

  useEffect(() => {
    axios.get("http://localhost:8000/master").then((res) => {
      setRowData(res.data);
    });
  }, []);

  return (
    <BaseTable
      title="Mastertabelle – Bauteile"
      rowData={rowData}
      zoom={zoom}
      setZoom={setZoom}
      nonEditableFields={["Revision"]}
      maxWidthMap={{ Kommentar: 500, Beschreibung: 500 }}
    />
  );
};

export default MasterTable;
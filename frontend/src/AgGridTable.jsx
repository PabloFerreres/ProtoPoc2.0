import React, { useEffect, useState } from "react";
import axios from "axios";
import BaseTable from "./components/BaseTable";

const AgGridTable = () => {
  const [rowData, setRowData] = useState([]);
  const [projektId, setProjektId] = useState(null);
  const [projektListe, setProjektListe] = useState([]);
  const [zoom, setZoom] = useState(1.0);

  useEffect(() => {
    axios.get("http://localhost:8000/projects").then((res) => {
      setProjektListe(res.data);
      if (res.data.length > 0) {
        setProjektId(res.data[0]);
      }
    });
  }, []);

  useEffect(() => {
    if (projektId) {
      axios.get(`http://localhost:8000/project/${projektId}`).then((res) => {
        setRowData(res.data);
      });
    }
  }, [projektId]);

  return (
    <div>
      <div style={{ marginBottom: 10 }}>
        <label htmlFor="projektDropdown">Projekt: </label>
        <select
          id="projektDropdown"
          value={projektId || ""}
          onChange={(e) => setProjektId(e.target.value)}
        >
          {projektListe.map((proj) => (
            <option key={proj} value={proj}>
              {proj.replaceAll("_Arma", "").replaceAll("_", " ")}
            </option>
          ))}
        </select>
      </div>
      <BaseTable
        title="Projektansicht – Armaturenliste"
        rowData={rowData}
        zoom={zoom}
        setZoom={setZoom}
        nonEditableFields={[
          "call_id",
          "Ort",
          "Revision",
          "Hersteller",
          "Material",
          "Gewicht",
          "Größe",
          "Spell",
          "Magische-Relevanz",
        ]}
        maxWidthMap={{ Kommentar: 500, Beschreibung: 500 }}
      />
    </div>
  );
};

export default AgGridTable;
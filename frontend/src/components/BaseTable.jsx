import React from "react";
import BaseViewTable from "./BaseViewTable";

const BaseTable = ({ rowData, title, zoom, setZoom, columnDefs, gridRef }) => {
  return (
    <BaseViewTable
      rowData={rowData}
      title={title}
      zoom={zoom}
      setZoom={setZoom}
      columnDefs={columnDefs}
      gridRef={gridRef} // ✅ gridRef weiterreichen
    />
  );
};

export default BaseTable;

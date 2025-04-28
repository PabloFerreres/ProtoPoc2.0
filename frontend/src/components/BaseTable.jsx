import React from "react";
import BaseViewTable from "./BaseViewTable";

const BaseTable = ({ rowData, title, zoom, setZoom, columnDefs, gridRef, rowHeight, saveLayout }) => {
  return (
    <BaseViewTable
      rowData={rowData}
      title={title}
      zoom={zoom}
      setZoom={setZoom}
      columnDefs={columnDefs}
      gridRef={gridRef}
      rowHeight={rowHeight}  // Weitergabe der festen Zeilenhöhe
      saveLayout={saveLayout}  // Weitergabe der saveLayout Funktion
    />
  );
};

export default BaseTable;

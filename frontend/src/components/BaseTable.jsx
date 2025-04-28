import React from "react";
import BaseViewTable from "./BaseViewTable";

const BaseTable = ({ rowData, title, zoom, setZoom, columnDefs }) => {
  return (
    <BaseViewTable
      rowData={rowData}
      title={title}
      zoom={zoom}
      setZoom={setZoom}
      columnDefs={columnDefs}
    />
  );
};

export default BaseTable;

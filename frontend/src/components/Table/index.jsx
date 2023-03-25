import React from "react";
import { useTable, useSortBy } from "react-table";

const ReactTable = ({ columns, data }) => {
    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        rows,
        prepareRow,
    } = useTable({
        columns,
        data,
    }, useSortBy);
    
    return (
        <>
        <table {...getTableProps()}>
          <thead>
            {headerGroups.map(headerGroup => (
              <tr {...headerGroup.getHeaderGroupProps()} key={headerGroup.id}>
                {headerGroup.headers.map(column => (
                  <th {...column.getHeaderProps(column.getSortByToggleProps())}
                        key={column.id}
                        className={
                            column.isSorted
                                ? column.isSortedDesc
                                ? "sort-desc"
                                : "sort-asc"
                            : ""
                        }
                        >
                    {column.render("Header")}
                </th>
                ))}
              </tr>
            ))}
          </thead>
          <tbody {...getTableBodyProps()}>
            {rows.map((row, i) => {
              prepareRow(row);
              return (
                <tr {...row.getRowProps()} key={i}>
                  {row.cells.map(cell => {
                    return <td {...cell.getCellProps()} key={cell.id}>
                                {cell.render("Cell")}
                            </td>;
                  })}
                </tr>
              );
            })}
          </tbody>
        </table>
        </>
      );

}
export default ReactTable
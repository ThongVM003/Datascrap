
# $csv = "D:\Work I guess\Datascrap\3.csv"
# $xlsx = "D:\Work I guess\Datascrap\3.xlsx"
# $delimiter = ","
# $excel = New-Object -ComObject excel.application
# $workbook = $excel.Workbooks.Add(1)
# $worksheet = $workbook.worksheets.Item(1)
# $TxtConnector = ("TEXT;" + $csv)
# $Connector = $worksheet.QueryTables.add($TxtConnector, $worksheet.Range("A1"))
# $query = $worksheet.QueryTables.item($Connector.name)
# $query.TextFileOtherDelimiter = $delimiter
# $query.TextFileParseType = 1
# $query.TextFileColumnDataTypes = , 1 * $worksheet.Cells.Columns.Count
# $query.AdjustColumnWidth = 1
# $query.Refresh()
# $query.Delete()
# $Workbook.SaveAs($xlsx, 51)
# $excel.Quit()


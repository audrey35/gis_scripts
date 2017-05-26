import xlrd
import csv
import arcpy

def arctable_to_csv(in_arctable,out_csv):
    # ArcTable (dbf or info) to xls
    xls = out_csv.split(".")[0] + ".xls"
    arcpy.TableToExcel_conversion (in_arctable, xls, "NAME", "CODE") # test.dbf => .xls
    # xls to CSV
    workbook = xlrd.open_workbook(xls)
    worksheet = workbook.sheet_by_name(out_csv.split("\\")[-1].split(".")[0])
    csvfile = open(out_csv, 'wb')
    writecsv = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for rownum in xrange(worksheet.nrows):
        writecsv.writerow(worksheet.row_values(rownum))
    csvfile.close()
    #arcpy.Delete_management(in_arctable)
    #arcpy.Delete_management(xls)

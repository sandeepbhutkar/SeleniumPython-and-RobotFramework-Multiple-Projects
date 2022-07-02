#ipw s ff sw

import openpyxl

path='F:\Selenium With Python\WriteData.xlsx'
workbook=openpyxl.load_workbook(path)
sheet=workbook.active
for r in range(1,2):     #from row 1 to 1
    for c in range(1,2):    #from column 1 to 1
        sheet.cell(row=r,column=c).value="Sandeepl"
workbook.save(path)

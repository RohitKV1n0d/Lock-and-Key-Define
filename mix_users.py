import xlrd
from xlwt import Workbook

loc = ("event-attendee-list.xlsx")
loc2 = ("All_data_1200.xlsx")




wb_w = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb_w.add_sheet('Sheet 1')



wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

wb2 = xlrd.open_workbook(loc2)
sheet2 = wb2.sheet_by_index(0)
sheet2.cell_value(0, 0)





for i in range(1,205):
    for j in range(1,202):
        if sheet2.cell_value(i, 1) == sheet.cell_value(j, 1) :
            sheet1.write(i, 0, sheet.cell_value(j, 2))
            sheet1.write(i, 1, sheet.cell_value(j, 3))  
            sheet1.write(i, 2, sheet.cell_value(j, 10)) #college
            sheet1.write(i, 3, sheet2.cell_value(i, 27))  #penalty
            sheet1.write(i, 4, sheet2.cell_value(i, 28))  #time





wb_w.save('win1.xls')


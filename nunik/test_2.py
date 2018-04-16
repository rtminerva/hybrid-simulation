from xlrd import open_workbook
import math as m
book = open_workbook('data.xlsx')
sheet = book.sheet_by_index(0)

time_x = []
current_y = []

for k in range(1,sheet.nrows):
    time_x.append(str(sheet.row_values(k)[1-1]))
    current_y.append(str(sheet.row_values(k)[2-1]))

time_xx = map(float, time_x)
current_yy = map(float, current_y)
print time_xx
print '********'
print current_yy

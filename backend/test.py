from soz_analizi import *
from xlrd import open_workbook

book = open_workbook('ex.xls',on_demand=True)
sheet = book.sheet_by_index(0)

file1 = open("out.txt","a")

for k in range(1,236):
    metn=sheet.cell_value(k, 4)
    cvb=metn_hecala(metn)
    file1.write(cvb)
    file1.write('\n')




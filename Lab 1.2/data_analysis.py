#!/usr/local/bin/python3

from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x):
    return x.value

work_book = load_workbook('data_analysis_lab.xlsx')
#sheet = work_book['Data']
#column_a=sheet['A'][1:]
column_a=work_book['Data']['A'][1:]
column_c=work_book['Data']['C'][1:]
column_d=work_book['Data']['D'][1:]

x_list=list(map(getvalue, column_a))
y1_list=list(map(getvalue, column_c))
y2_list=list(map(getvalue, column_d))

print(list(x_list))
#print(list(y1_list))
#print(list(y2_list))

pyplot.plot(x_list,y1_list,label="Temperature")
pyplot.plot(x_list,y2_list,label="Sun_Activity")
pyplot.legend()
pyplot.show()

#legend = pyplot.plot.legend(handles=['Day 1','Day 2'], title = "Legend")






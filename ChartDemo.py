'''
Created on 15-Feb-2017

@author: BALASUBRAMANIAM
'''
import os
from openpyxl import Workbook

from openpyxl.chart import (
    AreaChart,
    Reference,
    Series,
    BarChart3D,
)
wb=Workbook()
ws=wb.active
rows = [
    ['TraineeId', 'Test1', 'Test2'],
    [2324, 40, 30],
    [345, 90, 25],
    [4435, 80, 30],
    [5435, 78, 65],
    [6345, 90, 55],
    [7435, 50, 10],
]

for row in rows:
    ws.append(row)
    
chart =  BarChart3D()
chart.title = "Score Graph"
chart.style = 13
chart.x_axis.title = 'Trainee Id'
chart.y_axis.title = 'Marks(%)'
Reference()
cats = Reference(ws, min_col=1, min_row=1, max_row=7)
data = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=7)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)

ws.add_chart(chart, "F12")

path=os.getcwd()
wb.save(path+"/BarChartData.xlsx")

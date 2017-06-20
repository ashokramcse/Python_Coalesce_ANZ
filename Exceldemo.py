'''
Created on 20-Jun-2017

@author: BALASUBRAMANIAM
'''
import calendar
from openpyxl import Workbook
from pip._vendor.distlib.compat import raw_input
dirName="G:/Local Disk/Python/ANZ_Day4"
fileName=raw_input("Enter file Name")
filePath=dirName+"/"+fileName+".xlsx"
wb=Workbook()
i=1
for month in calendar.month_name:
    print(month)
    if not (len((str(month)))==0):
       wb.create_sheet(month+"_2017", i)
    i+=1
wb.save(filename=filePath)
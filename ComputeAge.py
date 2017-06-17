'''
Created on 16-Jun-2017

@author: BALASUBRAMANIAM
'''
from datetime import date
from pip._vendor.distlib.compat import raw_input
currDate=date.today()
print(date.today().strftime("%d\t%m\t%Y"))
dob = raw_input("Enter the DOB (dd-MM-yy)") 
slist = dob.split("-")
sdate = date(int(slist[2]),int(slist[1]),int(slist[0]))
print(sdate)
#find the difference
diff=currDate.year -sdate.year
print(type(diff))
print(diff)





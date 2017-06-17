'''
Created on 16-Jun-2017

@author: BALASUBRAMANIAM
'''
import calendar

#calformat = calendar.TextCalendar(calendar.SUNDAY)
#calformat.monthdatescalendar(2017, 6)
print (calendar.TextCalendar(calendar.MONDAY).formatmonth(2017,6, 0, 0))
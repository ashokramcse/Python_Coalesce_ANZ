#multiline comments
'''
Created on 16-Jun-2017

@author: BALASUBRAMANIAM
'''
from pip._vendor.distlib.compat import raw_input
import sys
ipAddress="172.89.97.98"
port=7890
strData='%s'
print("https://%s:%d" %(ipAddress,port))
print ("Anand says,'he\'s not well'")




'''
print ("Welcome to Python Training")
firstName= raw_input("Enter your First Name")
age=raw_input("Enter Age")
age_in_number=int(age)
title="Mr/Ms"
print("First Name=\t%s\t%s having age \t %d" %(title,firstName,age_in_number))
print(type(firstName))
print("Size of the variable %d" %(sys.getsizeof(firstName)))
'''
#complex number
complexNum1=8+5j
complexNum2=5+9j
print(complexNum1+complexNum2)
print(complexNum2.real)
print(complexNum2.imag)

#float data
interestRate=0.085
percRate=interestRate*100
print("InterinterestRate in %d" %(percRate))

#scientific data type 
data=3.e-2
print(data)
testData=1.9
print(int(testData))

#number to character
print(chr(67))

#binary data
print(bin(10))
print(hex(255))









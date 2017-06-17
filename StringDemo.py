'''
Created on 17-Jun-2017

@author: BALASUBRAMANIAM
'''
devInformation='''lists are the most versatile of Python's compound data types.
A list contains items separated by commas and enclosed within square brackets ([]).
To some extent, lists are similar to arrays in C.
One difference between them is that all the items belonging to a list can be of different data type.
'''

print(devInformation.capitalize())

name='Python' 
print(name.center(len(name)+10,'-'))#width,filler
print(name.ljust(20,'*'))
amount="4387"
print(amount.rjust(20,'*'))
name='Python\tTest'
print(name.expandtabs(tabsize=16))

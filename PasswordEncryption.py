'''
Created on 17-Jun-2017

@author: BALASUBRAMANIAM
'''
password='star'
#method 1 string to binary
binaryData=bin(int.from_bytes(password.encode(), 'big'))
print(binaryData)




#method 2 string to character to ordinal to binary
binaryList=[]

for ch in password:
    #print(bin(ord(ch)))
    binaryList.append(bin((ord(ch)) & (111)))
   
print(binaryList)


 



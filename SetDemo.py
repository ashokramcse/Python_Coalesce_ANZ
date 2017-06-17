'''
Created on 17-Jun-2017

@author: BALASUBRAMANIAM
'''
import random
portSet_device1={8080,90,78,72,3030,9001}
portSet_device2={425,80,78,1026,5127,9001}
newPortSet=portSet_device1.union(portSet_device2)
print(newPortSet)
commonPorts=portSet_device1.intersection(portSet_device2)
print(commonPorts)

idSet={""}
import base64
#generate random numbers
for i in range(100):
   idSet.add(base64.b64encode(str(random.
                                  randrange(10000000)).encode
                           (encoding='utf_8', errors='strict')))  
   
   
print(idSet)

'''
value=34438
encoded = base64.b64encode(str(value).encode
                           (encoding='utf_8', errors='strict'))
print(encoded)
'''



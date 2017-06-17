'''
Created on 17-Jun-2017

@author: BALASUBRAMANIAM
'''
import math

classArray={'classA':'10.0.0.1','classB':'172.16.0.1','classC':'192.168.0.1'}
def calculate(subnetClass,noOfHosts,startingIP):    
    print(subnetClass,noOfHosts,startingIP)
    print(math.log2(float(noOfHosts)))
    maskbit=math.ceil(math.log2(float(noOfHosts)
                              ))
    print("Mask Bits%d" %(maskbit))
    defaultAddr = classArray.get(subnetClass)
    if(defaultAddr==startingIP):
        print("Valid IP") 
        
    print("Borrowed Network bits%d" %(32-maskbit))
    return None

   
    
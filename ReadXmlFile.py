'''
Created on 26-Jun-2017

@author: BALASUBRAMANIAM
'''
from xml.dom import minidom

doc = minidom.parse("RouterInformation.xml")

routers=doc.getElementsByTagName("Router")

for router in routers:
    print(router.getElementsByTagName("HostName")[0].firstChild.data)
    interfaceData=router.getElementsByTagName("InterfaceNo")[0]
    print(interfaceData.firstChild.data)
    
    
    
    
    
    

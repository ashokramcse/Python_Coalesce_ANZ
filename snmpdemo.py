'''
Created on 18-Jun-2017

@author: BALASUBRAMANIAM
'''
#getcmd
from pysnmp.hlapi import *
g = getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget(('demo.snmplabs.com', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 
                                     'sysDescr', 0)))
print(next(g))

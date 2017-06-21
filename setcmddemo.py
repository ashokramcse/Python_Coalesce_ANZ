'''
Created on 20-Jun-2017

@author: BALASUBRAMANIAM
'''
from pysnmp.hlapi import *
g = setCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget(('demo.snmplabs.com', 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0), 'Linux i386'))
print(next(g))
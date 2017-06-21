'''
Created on 20-Jun-2017

@author: BALASUBRAMANIAM
'''
from pysnmp.hlapi import *
g = sendNotification(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget(('demo.snmplabs.com', 162)),
                     ContextData(),
                     'trap',
                     NotificationType(ObjectIdentity('IF-MIB', 'linkDown')))

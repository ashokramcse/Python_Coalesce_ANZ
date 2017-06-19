'''
Created on 19-Jun-2017

@author: BALASUBRAMANIAM
'''
#Router class definition
from pip._vendor.distlib._backport.tarfile import pwd
class Router:
    def __init__(self,hname,_link,_ipaddress,user,_vlan,maddr):
        self.hostname=hname
        self.link=_link
        self.ipaddress=_ipaddress
        self.userName=user       
        self.vlan=_vlan
        self.macAddress=maddr
    def set_pwd(self,pwd):
        self.password=pwd
        
    def get_pwd(self):
        return self.password
        
    def filter(self):
        print("filtering the IP addresses",self.hostname,
              self.link)

      
#Router Object
router1841=Router('localhost','up','10.10.9.1','user1',True,'0001.634A.1601')
router1841.set_pwd('test@123')
router1841.filter()
router2811 = Router('remotehost','down','10.10.9.31','user2',False,'0001.634B.1651')
router2811.set_pwd('anz@123')
router2811.filter()

#retrieve password for the device
print(router1841.get_pwd())





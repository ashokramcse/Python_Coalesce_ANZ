'''
Created on 19-Jun-2017

@author: BALASUBRAMANIAM
'''
#PC definition
class PC:
    def __init__(self,_link,_ipaddress,maddr):
        self.link=_link
        self.ipAddress=_ipaddress
        self.macAddress=maddr
    def set_location(self,loc):
        self.location=loc
    def get_location(self):
        return self.location
    
class Switch:
    def __init__(self,_ipaddress,_vlan,hname,maddr):
      
        self.ipAddress=_ipaddress
        self.vlan=_vlan
        self.hostName=hname
        self.macAddress=maddr
    def set_port(self,_port):
        self.port=_port
    def get_port(self):
        return self.port
    def set_pclist(self,pcData):
        self.pcList=pcData
    

#PC instances
pc0=PC('up','10.10.9.101','00D0.BD10.5C66')
pc0.set_location('InterCity Home City')
    
pc1=PC('up','10.10.9.100','00D0.BD10.697D')
pc1.set_location('InterCity Home City')

pcList=[pc0,pc1]
#switch instances
switch0_2954_20=Switch('10.10.9.2',True,'SwitchLab1',
                       '00D0.BD58.1747')
switch0_2954_20.set_pclist(pcList)

#Router class definition

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
    def set_switches(self,switchData):
        self.swichList=switchData
    
    def filter(self):
        print("filtering the IP addresses",self.hostname,
              self.link)

      
#Router Object
router1841=Router('localhost','up','10.10.9.1','user1',True,
                  '0001.634A.1601')
router1841.set_pwd('test@123')
router1841.set_switches(switch0_2954_20)
router1841.filter()
router2811 = Router('remotehost','down','10.10.9.31','user2',
                    False,'0001.634B.1651')
router2811.set_pwd('anz@123')
router2811.filter()

#retrieve password for the device
print(router1841.get_pwd())





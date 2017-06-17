'''
Created on 17-Jun-2017

@author: BALASUBRAMANIAM
'''
routerConfig={'userName':'user001','password':'537678abc',
              'host':['192.167.98.90','198.189.90.1']}
#print(routerConfig.keys())
#print(routerConfig.values())
#for(k,v) in routerConfig.items():
#    print(k,"\t",v)

listOfdevices=[{"device1":{'userName':'user002','password':'537788def',
              'host':['192.167.98.91','198.189.91.1']}},
               {"device2":{'userName':'user001','password':'537678abc',
              'host':['192.167.98.90','198.189.90.1']}},
               {"device3":{'userName':'user004','password':'237678def',
              'host':['192.169.98.90','198.189.190.1']}},
               {"device4":{'userName':'user005','password':'537688abc',
              'host':['192.167.91.27','198.189.127.1']}}]



#device={"device1":{'userName':'user1','password':'dbf678'}}

for item in listOfdevices:
    for (k,v) in item.items():
         print(k)
         for (k1,v1) in v.items():
             print(k1,"\t",v1)
             
         

     

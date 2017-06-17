'''
Created on 16-Jun-2017

@author: BALASUBRAMANIAM
'''
fileData=open('G:/test/NetworkData.csv','r')
ip_devaddr=list(fileData)
ipaddress=[]
devaddress=[]
for row in ip_devaddr:
    colData=row.split(',')
    ipaddress.append(colData[0])
    devaddress.append(colData[1])

#mapping ipaddress and device address
for iaddr in ipaddress:
    for devaddr in devaddress:
        print("SNMP walk %s%s" %(iaddr,devaddr))
        
        
urls=["http://localhost:11425","http://localhost:1001","http://localhost:8080",
     "http://localhost:80"]

for url in urls:
    data=url.split(":")
    if((int(data[2])>=1000)and(int(data[2])<=1024)):
       print("%s--->reserved port" %(data[2]))
    elif((int(data[2])>=10000)and(int(data[2])<=20000)):
        print("%s--->Game port" %(data[2]))
    else:
        print("%s---->not reserved port" %data[2])


        
        


   
   
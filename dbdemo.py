'''
Created on 19-Jun-2017

@author: BALASUBRAMANIAM
'''
import pymysql
from oopsdemo.RouterClass import PC,Switch
db=pymysql.connect(host="localhost",user="root",
                   passwd="vignesh",
                   db="networkdb")
cursor=db.cursor()
query="select * from PC"
cursor.execute(query)
rows = cursor.fetchall()
#print(rows)

#pc0=PC('up','10.10.9.101','00D0.BD10.5C66')
objList=[]
for row in rows:
    list=[]
    for col in row:
        print(col)
        list.append(col)
    list[0] = PC(list[3],list[1],list[2])
    objList.append(list[0])
    
#print(objList)

print("PC Data..............")
for pcInfo in objList:
    print(pcInfo.link,"\t",pcInfo.ipAddress,"\t",pcInfo.macAddress)

switch_cursor=db.cursor()
query="select * from switch"
switch_cursor.execute(query)
switch_rows=switch_cursor.fetchall()

switchList=[]
#_ipaddress,_vlan,hname,maddr
for row in switch_rows:
    list=[]
    for col in row:
        list.append(col)
    list[0]=Switch(list[1],list[3],list[0],list[2])
    switchList.append(list[0])

print(switchList)
pc_cursor=db.cursor()

for switch in switchList:
    print(switch.hostName)
    
    pc_cursor.execute("""select * from PC where 
    switch_host='%s'""" %(switch.hostName))
    rows=pc_cursor.fetchall()
    for row in rows:
        list=[]
        for col in row:
            print(col)
            list.append(col)
    list[0] = PC(list[3],list[1],list[2])
    switch.set_pclist(list[0])
#insert data to PC table

pcinsert_cursor=db.cursor()
query="""INSERT INTO PC(PCNO,
   IPADDRESS, MACADDRESS, link, switch_host)
   VALUES ('PC-4','192.168.30.1','00D0.B547.1678','UP',NULL)"""
try:
    pcinsert_cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()



  



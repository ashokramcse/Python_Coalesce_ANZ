'''
Created on 16-Jun-2017

@author: BALASUBRAMANIAM
'''
trainees=["T1","T2","T3"]
skillset=["C","Python","java"]
scores=[[6,7,8],[8,9,5],[9,7,5]]
print("\t%s" %(skillset))
i=0
for tscore in scores:    
    
    print("%s\t%s" %(trainees[i]," ".join(str(tscore))))
    i+=1 #i=i+1
   





#import filecmp

#print(filecmp.cmp("G:/test/EmployeeData.csv","G:/test/CustomerData.csv"))


#employeeData=open("G:/test/EmployeeData.csv",'r')
#customerData=open("G:/test/CustomerData.csv",'r')
'''
for data in list(employeeData):
    rowData=data.split(',')
    print(rowData[0]+"\t"+rowData[1]+"\t"+rowData[2])
'''
#employeeList=list(employeeData)
#customerList=list(customerData)

#for row in range(len(employeeList)):
#    print(employeeList[row]<customerList[row])








#empList= list(employeeData)
#print(empList[1])







#create dynamic list
#from pip._vendor.distlib.compat import raw_input
'''
empList=[]
for number in range(5):
   empList.append(raw_input("Enter Employee Name"))

for employee in empList:
    print("Reading the employee Name \t%s " %(employee))
    '''
'''
DataList=["http://192.168.2.72:8080",1,4.5,True,"shakthi"]
#reverse position
print(DataList[-2])

#slicing
print(DataList[-3:-1])

#_ variable name

#for _ in DataList:
#    print(_)



print(len(DataList))
#replication
test = DataList[4]+"\t"
print(test*4)
tempData=list(DataList[4])
for ch in tempData:
    print (ch)

corp1=['Google','IBM','VERIZON']
corp2=['Wellsfargo','Mercedes','ANZ']

for i in range(len(corp1)):
   print(corp1[i]+"\t"+corp2[i])

extractedList=[]
for data in DataList:
    if (type(data)==str):
        if (":" in data):
            portSet=data.split(":")
            print (portSet[2])
        
#print(extractedList)
#portList=extractedList[0].split(':');
#print(portList[2])


'''



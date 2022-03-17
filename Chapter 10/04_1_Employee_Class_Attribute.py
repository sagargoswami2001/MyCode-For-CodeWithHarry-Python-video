#Author: Prakash
import os

class Employee:
    company = "Google" #Class Attribute This is same for all objects  
    salary = "5000" #Class Attribute is predefined and will be used if instance attribute is not created 
                    #Instance attribute take priority over class Attribute
    
    
nEmployee = Employee()
mEmployee = Employee()
print(nEmployee.company)
print(mEmployee.company)

Employee.company = "YouTube"#Changing class Attribute Changes the attribute in all the object that is instantiated from that Class
print(nEmployee.company)
print(mEmployee.company)
                        #Instance attriute is Different for Each instance of a class(Object)
nEmployee.salary = 5400 #Instance attribute of nEmployee
mEmployee.salary = 5500 #Instance attribute of mEmployee

print(nEmployee.salary)
print(mEmployee.salary)
#Author: Prakash
import os

class Employee:
    company = "Google" #Class Attribute This is same for all objects  
    salary = "5000" #Class Attribute is predefined and will be used if instance attribute is not created 
                    #Instance attribute take priority over class Attribute During assignment and retrival
    
    
nEmployee = Employee()
mEmployee = Employee()
# print(nEmployee.company)
# print(mEmployee.company)

# Employee.company = "YouTube"#Changing class Attribute Changes the attribute in all the object that is instantiated from that Class
# print(nEmployee.company)
# print(mEmployee.company)
                        #Instance attriute is Different for Each instance of a class(Object)
nEmployee.salary = 5400 #Adding Instance attribute of nEmployee
# mEmployee.salary = 5500 #Adding Instance attribute of mEmployee

#if We Comment out the instance attributes then the class Attribute salary will be used for All objects

print(nEmployee.salary) #Instance Attribute is used that is created above
print(mEmployee.salary) #Class Attribute is used since no instance attribute is found
# print(mEmployee.background) # No Instance or Class attribute found so Error will be Thrown

'''
Attribute---------- ↴
                    ↓
            Instance Attribute (if Found then used, in not then Check for Class Attribute)
                    |
                    ↓
            Class Attribute (if found then used, else Throw Error)       

'''
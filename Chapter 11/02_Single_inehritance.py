#Author: Prakash
#This type of inheritance is single inheritance.

import os 

class Employee():   #-----------------------|
    company = "Google"                  #   |
                                        #   |------>This is a Base Class.
    def showDetail(self):               #   |
        print("This is an Employee")    #---|
        
class Programmer(Employee):     #-----------------------------------| #Here we are Inheriting From Base Class Employee
    company = "YouTube"                                         #   |
                                                                #   |------>This is a Derived Class.
    def showDetail(self):   #overwriting showdetail of base class.  |
        print("This is a Programmer")                           #   |      
                                                                #   |
    def getLang():  #Adding new attribute in Derived class      #   |
        print("They Specialize in Python.")         #---------------|
        
        
e = Employee()      #Instance of Base Class Employee
p = Programmer()    #Instance of Derived Class programmer

e.showDetail()      #Calling ShowDetail of the base class Employee
p.showDetail()      #Calling ShowDetail of the Derived class programmer

print(e.company)    #printing company of the base class Employee
print(p.company)    #printing company of the Derived class programmer
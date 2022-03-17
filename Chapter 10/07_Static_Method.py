#Author: Prakash
import os
from datetime import datetime #you can use datetime class of the datetime module.(Ignore/Optional)

class Employee:
    company = "Google"
    def getsalary(self): #Multiple arguments can be passed apart from Self
        print(f"in {self.company} Salary is {self.Salary}.") #

    @staticmethod
    def greet(): #Now this is a static method and needs no arguments, if we use Self we will get error here
        print("Yo, Bro!!")
        
    # def greet(self): #If we Omit self Argument then It won't run but we actually don't need self in this member function
    #                     #As we are only printing a string in it
    #     print("Yo, Bro!!")
    
    @staticmethod
    def PrintDateandTime():#(Ignore/Optional)
        now = datetime.now() #Getting date and Time from date and time Module (Ignore/Optional)
        print(f"Current Date and Time is: {now}")
        
employeeA = Employee()

employeeA.Salary = 551145

employeeA.getsalary()
'''     ↓    #above statement Get Converted to below one 
Employee.getsalary(employeeA)
'''
employeeA.greet() #this get converted to Employee.greet(employeeA) but we want to run it as Employee.greet()
                # for this we will have to use Static method decorator, which is used on line 9, so this will work fine 
employeeA.PrintDateandTime()#(Ignore/Optional)
'''
Static methods in Python are extremely similar to python class level methods, 
the difference being that a static method is bound to a class rather than the objects for that class.

This means that a static method can be called without an object for that class. 
This also means that static methods cannot modify the state of an object as they are not bound to it.

'''
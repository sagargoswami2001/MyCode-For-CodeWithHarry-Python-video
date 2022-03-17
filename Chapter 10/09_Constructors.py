#Author: Prakash
import os

class Employee:
    company = "Google"
    
    def __init__(self, Name, Initial, Salary, Division): #This is a constructor it's name has to be __init__,
        self.name = Name            # These are all attributes of instance objects
        self.intial = Initial       #These will be intialized as soon as object is created of class Employee
        self.salary = Salary        #
        self.division = Division    #

        print("Employee is Created!")
        
    def getDetails(self):
        print(f"Employee name: {self.name}\nSalary is {self.salary} in Division {self.division} uses Intials: {self.intial}.") #


#employeeA = Employee() # This throws an error: missing 4 required positional arguments
                                            #('Name', 'Initial', 'Salary', and 'Division')     
employeeA = Employee("Ymir", "Y", 503210, "YouTube") #As soon as we create object of employee class
                                                        # constructor is called automatically
employeeA.getDetails() #Calling getDetail function to print Object instance attributes



'''
Quick quiz answer:
Q1. Which function Prints "Employee is Created!" 
Ans. This being printed from constructor as soon as object is created the constructor is called.

2.  Which function Prints
    "
    Employee is Created!
    Employee name: Ymir
    Salary is 503210 in Division YouTube uses Intials: Y.
    "
Ans. This is getting printed When we are calling getDetails() of employeeA Object.
    
'''
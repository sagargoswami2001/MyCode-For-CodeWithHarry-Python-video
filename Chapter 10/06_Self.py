#Author: Prakash
import os

class Employee:
    company = "Google"
    def getsalary(self): #If we Don't Write self we would get an error because...See Line 11's Comment
        print(f"in {self.company} Salary is {self.Salary}.") #self.Salary pointing to the salary of obj in self which is employeeA
        #Self can be used to acccess both class attributes and instance attribute
        
employeeA = Employee() #Here we are Creating a new object instance of class Employee named employeeA
employeeA.Salary = 551145
employeeA.company = "Reddit"
employeeA.getsalary()# whenever we call a member function through a object instance
                        # then it's Object is automatically passed as a argument
                        #This statement gets converted to below statement internally, so 1 argument is passed automatically
                        
# Employee.getsalary(employeeA)#When We call member function through class Then we have to pass a valid object 

'''
NOTE: Often, the first argument of a method is called self. This is nothing more than a convention: 
the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers

'''
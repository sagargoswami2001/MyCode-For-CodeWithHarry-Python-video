#Author: Prakash
import os

class Employee:
    company = "Ninja Company"
    #signature = "A"
    
    def getsalary(self, signature): #Multiple arguments can be passed apart from Self
                                    #Self is being passed automatically and we are manually passing sign...
                                    #Note signature doesn't need to be accessed through self as it is passed manually form the calll
        print(f"in {self.company} Salary is {self.Salary}, Which have Intials {signature}.")
        
employeeA = Employee()
employeeA.Salary = 551145
employeeA.getsalary("Thanks") #Passsing Signature and self is automatically being passed
#        ↓     #above statement Get Converted to below one 
#Employee.getsalary(employeeA, "Thanks")
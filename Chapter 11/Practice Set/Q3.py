#Practice set Q3
#Author: Prakash

import os 

class Employee:
    salary = 1200
    increment = 1.5
    
    @property   
    def salaryAfterIncrement(self):  
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self, val):
        self.increment = val/self.salary

e = Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 2000

print(e.salary)
print(e.salaryAfterIncrement)
print(round(e.increment, 3))
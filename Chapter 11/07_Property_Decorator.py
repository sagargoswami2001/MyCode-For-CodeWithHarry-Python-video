import os

'''
A decorator function is basically a function that adds new functionality to a function that is passed as argument. 
Using a decorator function is like adding chocolate sprinkles to an ice cream ?. It lets us add new functionality 
to an existing function without modifying it.
'''
class Employee():
    company = "POCO"
    salary = 5000
    salaryBonus = 500
    # totalSalary = 6000
    
    @property   #property decorator(getter) is used to get a method to be perceived as property
    def totalSalary(self):  #This is a perceived as property instead of Method
        return self.salary+self.salaryBonus
    
    @totalSalary.setter #setter function is used to set The salaryBonus as we try to change totalsalary
    def totalSalary(self, val): #Here we change salary and then use this function to
        self.salaryBonus = val - self.salary    #minus salary from it. and whatever value is left will be salaryBonus
'''
@getter and @setter
The Methdo name with @property decorater is called getter method
@setter method is used to set proerties in class
'''     
    
e = Employee()
print(e.totalSalary)    #since this is not perceived as function but rather as property due to this doesn't require ()
                        #Since this is property we can change it just like property
                        
e.totalSalary = 5500 # if we change this property then we will have to do something so that it is changed as salary+salaryBonus
                    #for this we will have to use setter function

print(e.salary)
print(e.salaryBonus)
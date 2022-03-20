#Author: Prakash

'''
The super() builtin returns a proxy object (temporary object of the superclass) that allows us to access methods 
of the base class.

Use of super()
In Python, super() has two major use cases:

1. It Allows us to avoid using the base class name explicitly
2. Working with Multiple Inheritance


super() is generally used for runing constructor of Base class

In the case of single inheritance, we use super() to refer to the base class.
'''
import os 

class Person(): 
    country = "India"
    
    def __init__(self):
        print("Initializing Person...\n")
    
    def breath(self): #3. This method is ran by super() of employee and control return to employee
        print("Person Breathing....")
        
class Employee(Person):
    company = "Jaguar"
    
    def __init__(self):
        super().__init__()  #Here Super() is calling constructor of Person
        print("Initializing Employee...\n")
    
    def getSalary(self):
        print("Jaguar is a TATA Company.")
        
    def breath(self):
        super().breath() #super() Method is used to access the super/Parent class of a derived class 
                        #2. once we reach breath method of Employee we see another super method which says
                        #   to run the breath() method of it's parent class(Person)
                        
                        #4. once control Return after calling the method of parent classes attribute breath then 
                        # it will execute breath of This class and control will return to Programmer
        print("i am employee and i am Breathing in style....")
        
class Programmer(Employee):
    
    def __init__(self):
        super().__init__() #Here Super() is calling constructor of Employee
        print("Initializing Programmer...\n")               

    def getSalary(self): 
        print("We are Bathing in Dollars.")
    
    def breath(self):  
        super().breath() #super() Method is used to access the super/Parent class of a derived class
                        #1.This statement says to run the breath() method of it's parent class(Employee)
                        
                        #5. once control Return after calling the method of parent classes attribute breath then 
                        # it will execute breath of This class.
        print("i am Programmer and i don't know why i am Breathing....")
        
        
# p = Person()
# p.breath()

# e = Employee()
#e.breath()

pr = Programmer()
pr.breath()

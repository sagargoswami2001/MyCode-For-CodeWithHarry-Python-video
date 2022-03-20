import os

class Employee():
    company = "Apsara"
    salary = 500
    location = "mumbai"
    
    # def changeCompany(self, comp):
    #     self.company = comp #This will create a instance attribute and not change the class attribute company
    
    # Method 1: for changing class attribute
    # def changeCompany(self, comp):
    #     self.__class__.company = comp   #This will change the class attribute which in return changes the instace attribute
    
    # Method 2: for changing class attribute
    '''
    A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class 
    instance, much like staticmethod.

    The difference between a static method and a class method is:

    1.Static method knows nothing about the class and just deals with the parameters
    2.Class method works with the class since its parameter is always the class itself.
    
    Class method: Used to access or modify the class state. In method implementation, if we use only class variables, 
    then such type of methods we should declare as a class method. The class method has a cls parameter which refers 
    to the class.
    '''
    @classmethod
    def changeCompany(cls, comp): #Here we are not passing self instance but The class instance itself by cls This method will 
                                    #Require a Class Method decorater just like static method
        cls.company = comp
    
e = Employee()
print(e.company)

e.changeCompany("Tesla")

print(Employee.company) 
print(e.company)

#Author: Prakash
#This type of inheritance is Multiple inheritance.

import os 

class Employee(): #-------------------------|
    company = "CD Projekt Red"  #           |======> First Base Class
    ecode = 155 #---------------------------|
    
class Freelancer():
    company = "Bathesda Game studio"    #---------------------------|
    level = 0   #                                                   |======> Second Base Class
                #                                                   |
    def UpgradeLevel(self): #                                       |
        self.level += 1 #-------------------------------------------|

#Whichever Class is inherited first will be given priority while accessing method and attributes
class programmer(Employee, Freelancer):#----------------------------|
    name = "Manique"    #-------------------------------------------|=> Derived class Inheriting from both Employee and Freelancer
    
p = programmer() #Instance of Programmer class which inherit from both Employee and Freelancer class
print(p.company)    #Here there is ambiguity in printing company as it is defined in both class from which
                    #We are inheriting so company is printed from class that is inherited first
                    #In this case from Employee Class "CD Projekt Red is printed".
                    
print(p.level)  #Programmer class inherit level attribute from Freelancer base class

p.UpgradeLevel()    
print(p.level)

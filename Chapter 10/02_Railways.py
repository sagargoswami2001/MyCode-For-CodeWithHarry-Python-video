#Author: Prakash
import os

class RailwayForm:
    formType = "Railway Form"   #Class Data member
    
    def printData(self):        #Class Member function
        print(f"Name is {self.name}")
        print(f"Train is {self.Train}")
        
zaphApplication = RailwayForm() #Instantiating Object "zaphApplication"

zaphApplication.name = "ZAPHKILL"           #Attributes of RailwayForm
zaphApplication.Train = "CRAP Express"      #-----------------------------

zaphApplication.printData()     #Behaviour of zaphApplication


'''
For Clarity 

Objects consist of attributes and methods.

A class is the blueprint from which objects are created.

Within the class you'll define the common attributes and methods of the object(s) you wish to use in your program.

Attributes are 'values' or 'things' that all objects from that class will have in common. But they do not have to be the same!

Methods are specific functions which may be performed on that object.

'''
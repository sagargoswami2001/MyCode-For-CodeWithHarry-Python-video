# Practice set Q1
#Author: Prakash

import os 

class Programmer:
    company = "Microsoft"
    
    def __init__(self, Name, Product):
        self.name = Name
        self.product = Product
    
    def printDetails(self):
        print(f"In {self.company} Employee Name is {self.name} and Their Product is {self.product}."  )


david = Programmer("David", "DirectX")
laura = Programmer("Laura", ".NET CORE")

david.printDetails()
laura.printDetails()
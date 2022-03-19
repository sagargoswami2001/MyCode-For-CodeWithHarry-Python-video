# Practice set Q1
#Author: Prakash

import os 

class Programmer:
    company = "Microsoft"
    
    def printDetails(self):
        print(f"Employee Name is {self.Name}"  )

programmer1 = Programmer()
programmer1.Name = "David"
programmer1.printDetails()

programmer2 = Programmer()
programmer2.Name = "Laura"
programmer2.printDetails()

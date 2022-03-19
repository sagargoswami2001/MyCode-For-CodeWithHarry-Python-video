# Practice set Q5
#Author: Prakash

import os 

class Train:
    departmentOfGOI = "Indian Railways"
    
    def __init__(self, NameOfTrain, fair, seats):
        self.NameOfTrain = NameOfTrain
        self.fair = fair
        self.seats = seats 
    
    def bookTicket(self):
        
        if(self.seats>0):
            print(f"congratulation, your ticket is booked, Your seat no. is {self.seats}")
            self.seats = self.seats-1
        else:
            print(f"All seats full, your ticket can't be booked")
            
    def getStatus(self):
        print("********************************************************")
        print(f"The Name of the train is {self.NameOfTrain}")
        print(f"available seats in train is {self.seats}")
        print("********************************************************")
        
    def fairInfo(self):
        print(f"The fair of the train is {self.fair}")
    
intercity = Train("Intercity Ex1", "Rs.500", 1)

intercity.getStatus()
intercity.fairInfo()

intercity.bookTicket()
intercity.getStatus()

intercity.bookTicket()
intercity.getStatus()
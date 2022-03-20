## Chapter 10 Practice set Q5
#Author: Prakash

import os 

class Train:
    departmentOfGOI = "Indian Railways"
    
    def __init__(self, NameOfTrain, fair):
        self.NameOfTrain = NameOfTrain
        self.fair = fair
    
    def bookTicket(self):
        
        if(len(self.seatList)>0): #Checking if len of list is greater then 0
            print(f"congratulation, your ticket is booked, Your seat no. is {self.seatList[-1]}") #printing last element of the list, which is accessed by index[-1]
            del self.seatList[-1] #Deleting the last value of the list which is booked
        else:
            print(f"All seats full, your ticket can't be booked")
            
    def getStatus(self):
        print("********************************************************")
        print(f"The Name of the train is {self.NameOfTrain}")
        print(f"available seats in train is")
        print(self.seatList)
        print("********************************************************")
        
    def fairInfo(self):
        print(f"The fair of the train is {self.fair}")
        
    def cancelTicket(self, ticketno):
        self.seatList.append(ticketno)
        print("Your Ticket has been cancelled.")
    
intercity = Train("Intercity Ex1", "Rs.500")
intercity.seatList = [1,2] #Making a class attribute seatlist which can be accessedby self

intercity.getStatus()
intercity.fairInfo()

intercity.bookTicket()
intercity.getStatus()

intercity.bookTicket()
intercity.getStatus()

intercity.bookTicket()
intercity.cancelTicket(2) #canceling second ticket

intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()

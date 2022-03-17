#Author: Prakash
import os

class Remote:
    pass

'''
Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only 
on usage of it,Through the process of abstraction in Python, a programmer can hide all the irrelevant data/process of an 
application in order to reduce complexity and increase efficiency.

user or programmer need not know all the detail of implementation of class in order to use it

'''
class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveForward(self):
        pass
    def moveBackward(self):
        pass


remote1 = Remote()
player1 = Player()
if (remote1.pressLeft()):
    player1.moveLeft()
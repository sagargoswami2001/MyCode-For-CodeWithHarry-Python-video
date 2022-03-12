# Snake, water or gun game in Python
#Author: Prakash

'''
This just like stone paper scissor. Both the players should keep the gestures simultaneously. 
The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
'''


import os 
import random #Python Random Module

'''
This module implements pseudo-random number generators for various distributions.

For integers, there is uniform selection from a range. 
For sequences, there is uniform selection of a random element, 
a function to generate a random permutation of a list in-place, 
and a function for random sampling without replacement.

'''

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
        
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
    

print("PC: Snake(s), Water(w) or Gun(g)? ") #PC use random option he wants b/w three

randNum = random.randint(1,3)
if randNum == 1:
    comp = "s"
elif randNum ==2:
    comp = "w"
elif randNum == 3:
    comp = "g"
else:
    print("Invalid Option.")


you = input("Player: Snake(s), Water(w) or Gun(g)?n\nEnter you choice: ") #Asking Player 2 which option he wants b/w three and taking input

gamestatus = gameWin(comp, you)

print(f"Computer Chose {comp} and You chose {you}")

if (gamestatus==None):
    print("Game Tie")
elif(gamestatus):
    print("Congratulations, You've won the game!")
else:
    print("You've lost the game, Better luck next time.")

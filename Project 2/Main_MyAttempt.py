#Project 2
#author Prakash

import os 
import random

randomNumber = random.randint(0, 100)
userguess = None
guesscount = 0

while(userguess != randomNumber):
    userguess = int(input("Enter Your Guess: "))
    guesscount = guesscount + 1
    
    if(userguess>randomNumber):
        print("Your Guess is Too High, Pick a Lower Number.")
        
    elif(userguess<randomNumber):
        print("Your Guess is Too Low, Pick a Higher Number.")
        
    elif(userguess==randomNumber):
        print("Woah! You guessed it correctly!")
        
print(f"You took {guesscount} attempts to guess the no. correctly.")

with open("Project 2//High_Score", "r") as f:
    High_Score = int(f.read())
    
if(High_Score>guesscount):
    print("Wow! Congratulations, You have made a new HiGH SCORE.")
    
    with open("Project 2//High_Score", "w") as f:
        f.write(str(guesscount))
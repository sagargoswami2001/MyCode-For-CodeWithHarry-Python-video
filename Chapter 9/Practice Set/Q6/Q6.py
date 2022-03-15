#Practice set Q6
#Author: Prakash
import os

with open("Chapter 9//Practice Set//Q6//log.txt", "r")as f:
    content = f.read().lower()#Content raed from file is lowercased so case sensitivity don't throw an error
    
if "python" in content:
    print("python is Present.")
else: 
    print("No python found")
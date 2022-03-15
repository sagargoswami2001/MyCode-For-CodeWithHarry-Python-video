#Practice set Q8
#Author: Prakash
import os

with open("Chapter 9//Practice Set//Q8//this.txt", "r")as f:
    content = f.read()
    
f = open("Chapter 9//Practice Set//Q8//this-Copy.txt", "w")

f.write(str(content))

f.close()

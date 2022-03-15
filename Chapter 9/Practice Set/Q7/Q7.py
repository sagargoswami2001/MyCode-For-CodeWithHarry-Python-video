#Practice set Q7
#Author: Prakash
import os

content = 'True'
i = 0

with open("Chapter 9//Practice Set//Q7//log.txt", "r")as f:
    while content:
        i = i+1
        content = f.readline().lower()#Content raed from file is lowercased so case sensitivity don't throw an error
        
        if "python" in content:
            print(content)
            print("python is Present.")
            print("on Line: ",i)
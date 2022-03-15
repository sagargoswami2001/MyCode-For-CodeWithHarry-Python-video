#Practice set Q1
#Author: Prakash
import os 

f = open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q1//poem.txt", 'r')
t = f.read()

if "Twinkle" in t:
    print("Twinkle is present.")
else:
    print("Twinkle isn't present.")
f.close()

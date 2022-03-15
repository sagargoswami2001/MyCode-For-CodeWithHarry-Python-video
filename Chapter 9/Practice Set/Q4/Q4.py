
#Practice set Q4
#Author: Prakash
import os 

with open(f"D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q4//Weird.txt", 'r') as f:
    content = f.read()
content = content.replace("donkey", "######")

with open(f"D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q4//Weird.txt", 'w') as f:
    f.write(content)
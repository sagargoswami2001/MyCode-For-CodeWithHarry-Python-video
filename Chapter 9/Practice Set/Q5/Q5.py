
#Practice set Q5
#Author: Prakash
import os 

words = ["donkey", "danky" , "funky" , "monkee", "shonky" , "swanky" , "wonky", "mcconkey"]

with open(f"D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q5//Weird.txt", 'r') as f:
    content = f.read()
    
for word in words:
    content = content.replace(word, "^&%$(&*")
    with open(f"D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q5//Weird.txt", 'w') as f:
        f.write(content)
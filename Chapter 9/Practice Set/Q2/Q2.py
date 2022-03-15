#Practice set Q2
#Author: Prakash
import os 

def game():
    hs = int(input("Enter Your Score: "))
    return hs

score = game()

with open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q2//HiScore.txt", 'r')as f:
    hiscorestr = f.read()

if hiscorestr == '':
    with open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q2//HiScore.txt", 'w')as f:
            f.write(str(score))

elif (score > int(hiscorestr)):
    with open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q2//HiScore.txt", 'w')as f:
        f.write(str(score))
        

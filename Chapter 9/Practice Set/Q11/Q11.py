#Practice set Q11
#Author: Prakash
import os

with open("Chapter 9//Practice Set//Q11//File_to_Rename.txt", "r")as f:
    content = f.read()
    
with open("Chapter 9//Practice Set//Q11//Renamed_by_python.txt", "w")as f:
    f.write(content)
    
os.remove("Chapter 9//Practice Set//Q11//File_to_Rename.txt")
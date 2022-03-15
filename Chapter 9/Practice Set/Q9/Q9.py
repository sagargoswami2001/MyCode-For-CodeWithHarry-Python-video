#Practice set Q9
#Author: Prakash
import os


with open("Chapter 9//Practice Set//Q9//this.txt", "r")as f:
    content = f.read()
    
with open("Chapter 9//Practice Set//Q9//this-Copy.txt", "r")as f:
    content1 = f.read()
    
if(content==content1):
    print("this.txt and this-copy.txt contains the same content.")
else:
    print("this.txt and this-copy.txt doesn't contains the same content.")

#Python program to Open and appending into file
#Author: Prakash

import os 
'''
With the “With” statement, you get better syntax and exceptions handling.

“The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks.”

In addition, it will automatically close the file. The with statement provides a way for ensuring that a clean-up is always used
'''


with open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//05_with//sample1.txt", 'r') as f:
    a = f.read()
    
#can also be open in write mode

# with open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//05_with//sample1.txt", 'w') as f:
#     a = f.write("Jhakkas == Jackass")
    
print(a)
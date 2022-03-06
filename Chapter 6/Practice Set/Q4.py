#Solution of Practice Set Q4

import os 

Username = input("Enter Your Username: ")

Username_length = len(Username)
# print(Username_length) # to check length 

if(Username_length<10): 
    print('Username: "', Username, '"has a length of Less then 10')
else:
    print('Username: "', Username, '" has a length of Greater then 10')
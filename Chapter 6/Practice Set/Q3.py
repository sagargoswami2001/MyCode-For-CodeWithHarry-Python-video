#Solution of Practice Set Q3

import os 

Spam = False
Email = input("Enter the Message: ")

if("Make a lot of money " in Email):
    Spam = True
elif("Buy now "  in Email):
    Spam = True
elif("Subscribe This"  in Email):
    Spam = True
elif("Click This"  in Email):
    Spam = True
else:
    Spam = False
    
if(Spam):
    print("Spam Detected")
else:
    print("No Spam Keyword Detected")
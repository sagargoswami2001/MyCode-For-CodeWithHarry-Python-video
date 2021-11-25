import os 

Spam = False
Comment = input("Enter the Message: ")

if("Make a lot of money " in Comment):
    Spam = True
elif("Buy now "  in Comment):
    Spam = True
elif("Subscribe This"  in Comment):
    Spam = True
elif("Click This"  in Comment):
    Spam = True
else:
    Spam = False
    
if(Spam):
    print("Spam Detected")
else:
    print("No Spam Keyword Detected")
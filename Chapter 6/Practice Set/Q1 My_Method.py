#Solution of Practice Set Q1

import os 

Num1 = int(input("Enter No.1: "))
Num2 = int(input("Enter No.2: "))
Num3 = int(input("Enter No.3: "))
Num4 = int(input("Enter No.4: "))

if(Num1>Num2):
    if(Num1>Num3):
        if(Num1>Num4):
            print("Num1: ", Num1 , "is the Greatest No.")
        else:
            print("Num4: ", Num4 , "is the Greatest No.")
            
elif(Num2>Num3):
    if(Num2>Num4):
        print("Num2: ", Num2 , "is the Greatest No.")
    else:
        print("Num4: ", Num4 , "is the Greatest No.")
            
elif(Num3>Num4):
    print("Num3: ", Num3 , "is the Greatest No.")
else:
    print("Num4: ", Num4 , "is the Greatest No.")
            
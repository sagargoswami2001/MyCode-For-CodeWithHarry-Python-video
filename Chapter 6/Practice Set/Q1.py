#Solution of Practice Set Q1

import os 

Num1 = int(input("Enter No.1: "))
Num2 = int(input("Enter No.2: "))
Num3 = int(input("Enter No.3: "))
Num4 = int(input("Enter No.4: "))

if(Num1>Num4): 
    L1 = Num1
else:
    L1 = Num4

if(Num2>Num3):
    L2 = Num2
else:
    L2 = Num3

##printing greatest no as String 
if(L1>L2):
    print(str(L1)+ " is Greatest")
else:
    print(str(L2)+ " is Greatest")


##printing greatest no as int
if(L1>L2):
    print(L1, " is Greatest")
else:
    print(L2, " is Greatest")
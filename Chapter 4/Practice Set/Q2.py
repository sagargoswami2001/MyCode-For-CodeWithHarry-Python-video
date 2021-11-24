#Solution of Practice Set Q2

import os
 #Can be sorted without converting to string but you should convert to int just to be safe

S1 = int(input("Enter Marks Of Studnets 1:" ))
S2 = int(input("Enter Marks Of Studnets 2:" ))
S3 = int(input("Enter Marks Of Studnets 3:" ))
S4 = int(input("Enter Marks Of Studnets 4:" ))
S5 = int(input("Enter Marks Of Studnets 5:" ))
S6 = int(input("Enter Marks Of Studnets 6:" ))

myFruits = [S1,S2,S3,S4,S5,S6]#
myFruits.sort()

print(myFruits) 
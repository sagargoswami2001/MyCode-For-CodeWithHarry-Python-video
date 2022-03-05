#Solution of Practice Set Q2

import os
#Can be sorted without converting to string but you should convert to int just to be safe

S1 = int(input("Enter Marks Of Student 1:" ))
S2 = int(input("Enter Marks Of Student 2:" ))
S3 = int(input("Enter Marks Of Student 3:" ))
S4 = int(input("Enter Marks Of Student 4:" ))
S5 = int(input("Enter Marks Of Student 5:" ))
S6 = int(input("Enter Marks Of Student 6:" ))

Students = [S1,S2,S3,S4,S5,S6] # sorted marks of 6 students
Students.sort()

print(Students) 
# #Practice set Q8
#Author: Prakash

import os 

def table(x):
    for i in range (1,11):
        print(f"{x} X {i} =", i*x)


x = int(input("Enter a no. to print it's multiplication table: ")) 

table(x)
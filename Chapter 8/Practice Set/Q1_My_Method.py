#Practice set Q1
#Author: Prakash

import os

def largestno(x, y, z):
    
    if(x>y and x>z):
        print(f"{x} is Largest Number among three.")
    elif(y>x and y>z):
        print(f"{y} is Largest Number among three.")
    elif(z>x and z>y):
        print(f"{x} is Largest Number among three.")
    else:
        print("Couldn't determined largest either no. are repeated same or invalid no.")

x = int(input("Enter x no. ")) 
y = int(input("Enter y no. "))
z = int(input("Enter z no. "))

print(x,y,z)

largestno(x, y, z)
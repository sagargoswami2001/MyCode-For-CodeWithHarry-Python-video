#Practice set Q4
#Author: Prakash

import os 

prime = True

no = int(input("Enter a no. to find if it's prime or not: ")) #Getting a no. from user and casting to int

for i in range(2, no):
    if(no%i == 0):
        prime = False
        
if(prime):
    print(f"{no} is Prime no")
else:
    print(f"{no} is not a Prime no")
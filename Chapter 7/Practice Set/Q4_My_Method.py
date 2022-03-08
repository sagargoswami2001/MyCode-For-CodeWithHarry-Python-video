#Practice set Q4
#Author: Prakash

import os 

no = int(input("Enter a no. to find if it's prime or not: ")) #Getting a no. from user and casting to int

for i in range(2, no):
    if(no==0 or no==1): #if no is either 1 or 0 then it is not a prime no.
        print(f"{no} is not prime")
        break
    elif (no%i == 0 and no%2 == 0): #if no is divisible by i or 2 then it is not prime no
        print(f"{no} is not a prime no.")
        break
    else:
        print(f"{no} is prime")
        break



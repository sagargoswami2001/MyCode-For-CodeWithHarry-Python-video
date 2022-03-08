#Practice set Q5
#Author: Prakash

import os 

sum = 0

no = int(input("Enter a no. to find sum of natural no. till it: ")) #Getting a no. from user and casting to int

for i in range (1, no+1):
    sum+=i
    
print(f"Sum of first {no} natural numbers is: {sum}")

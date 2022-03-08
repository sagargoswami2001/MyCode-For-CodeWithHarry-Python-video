#Practice set Q6
#Author: Prakash

import os 

no = int(input("Enter a no. to find if it's prime or not: ")) #Getting a no. from user and casting to int
factorial_no = 1

i = no
while(i > 0):
    factorial_no = (factorial_no)*i # factorial of n = n*(n-1)*(n-2)*....n-(n-1) or 1x2x3....Xn
    i-=1
    
print(f"Factorial of {no}! is {factorial_no}")
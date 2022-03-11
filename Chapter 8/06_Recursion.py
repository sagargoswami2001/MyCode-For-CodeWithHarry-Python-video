# A Prorgram to show recursions in Python
#Author: Prakash

'''Recursion (adjective: recursive) occurs when a thing is defined in terms of itself or of its type - Wikipedia'''

#Recursion in Python
#In Python, we know that a function can call other functions. 
# it is even possible for the function to call itself. this is known as recursive functions.
import os 

#The factorial function (symbol: !) says to multiply all whole numbers from our chosen number down to 1.
# ex. factorial of no 4 = 4x3x2x1 which will be 24
# factorial 4 can be written as 4!


#By iteration
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return(product)


#By recursion
def factorial_recursive(n):
    
    if n==0 or n==1:
        return 1
    
    return n*factorial_recursive(n-1)

f = factorial_iter(5)
print(f)

f1 = factorial_recursive(5)
print(f1)

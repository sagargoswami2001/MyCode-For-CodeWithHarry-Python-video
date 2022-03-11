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

def factorial(number):
    if(number == 0 or number == 1): #Base Condition once the value is 1 function doesn't get called anymore
        return 1
    
    return (number*factorial(number-1)) 
    #here here factorial is * with another factorial function call while decrementing number by 1
    #This will be repeated till value is 1

num = int(input("Enter a no: ")) # getting a str value from user and casting it to int
# num = 5
print("Factorial of ", num, "is ", factorial(num)) #passing the user's entered value in factorial function

'''
NOTE: Be careful while using recursions:
1.  Recursive programs can fail to terminate. 
    Remember that your function must have code that handles the termination conditions. 
    That is, there must be some way for the function to exit without calling itself again.
    
2.  Stack Overflow. Remember that every function is a separate task that the computer must keep track of. 
    The computer manages a list of tasks that it can maintain, 
    but this list only has a limited amount of space. Should a recursive function require many copies of 
    itself to solve a problem, the computer may not be able to handle that many tasks, causing a system 
    error.

3.  Out of Memory Error. All of the functions we have shown here have used pass by value. 
    That means that every time a function is called it must allocate computer memory to copy
    the values of all the parameter variables. If a recursive function has many parameters, 
    or these parameters are memory intensive, the recursive calls can eat away at the computers
    memory until there is no more, causing a system error.
'''

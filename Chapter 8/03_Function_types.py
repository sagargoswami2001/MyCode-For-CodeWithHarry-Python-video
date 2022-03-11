'''
TYPES OF FUNCTIONS IN PYTHON

There are three types of functions in Python:

Built-in functions, min() to get the minimum value, print() to print an object to the terminal, and range() etc.
User-Defined Functions (UDFs), which are functions that users create acc. to their needs
Anonymous functions, which are also called lambda functions because they are not declared with the standard def keyword.

in 01, 02 we used user defined function using def as well as builin like print()
'''
import os


#User Defined Function
def greeting(name):
    print(f"Good Morning, {name}")


name = input("Enter a name: ")
greeting(name)


#Built-in functions
no = 4.64535364

print(round(no, 2)) #Built-in function to round of a float value 

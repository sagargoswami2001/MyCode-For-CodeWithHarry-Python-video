#Taking_Multiple_inputs_in_Python

#Author: Prakash

import os 

''' 
in Python user can take multiple values or inputs in one line by two methods. 
1. Using split() method
2. Using List comprehension

1. Using split() method: This function helps in getting multiple inputs from users. It breaks the given input by the
specified separator. If a separator is not provided then any white space is a separator. 
Generally, users use a split() method to split a Python string but one can use it in taking multiple inputs.

Syntax : input().split(separator, maxsplit)
'''

# x, y, z = input("Enter three Numbers: ").split() # This method works with string since split function splits strings
#                                                 #But we can't do typecasting here. we have to seperately typecast x,y,z
# x = int(x)
# y = int(y)
# z = int(z)

'''
2. Using List comprehension: List comprehension is an elegant way to define and create list in Python. 
We can create lists just like mathematical statements in one line only. 
It is also used in getting multiple inputs from a user. 

we can also typecast them as shown below
'''


#
x, y, z = [int(x) for x in input("Enter three values: ").split()]


print(x,y,z)
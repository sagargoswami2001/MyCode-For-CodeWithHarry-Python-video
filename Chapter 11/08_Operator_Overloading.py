import os 

'''
You can change the meaning of an operator in Python depending upon the operands used

Python operators work for built-in classes. But the same operator behaves differently with different types. 
For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.

This feature in Python that allows the same operator to have different meaning according to the context is called 
operator overloading.


NOTE: Method which are written as: __methodNAme__ are known as Dunder Methods
'''

class Number():
    def __init__(self, num):
        self.num = num
        
    def __add__(self, num2): #we have made a custom datatype/class which defines it's own add operator which returns
        print("Let's Add")  #Whatever we define(it can even be hard value of some expression evaluated) 
        return self.num + num2.num #it returns sum of it own num(n1's) + num2's num(n2's)
    
    def __mul__(self, num2):
        print("Let's Multiply")
        return self.num * num2.num
    
n1 = Number(4)
n2 = Number(6)
sum = n1 + n2   #Here + have a custom definition that we have defined using dunder __add__ method which takes two parameter
#if we don't define __add__ then it will throw an error as in class n1+n2 isn't defined because n1 and n2 are objects
print(sum)

mul = n1*n2
print(mul)

'''
NOTE:   OPERATORS IN PYTHON CAN BE OVERLOADED WITH THE HELP OF DUNDER METHODS
        THIS IS DEFINED IN PYTHON DOCUMENTATION THAT IF YOU WANT TO OVERLOAD + THEN YOU HAVE TO USE __add__ 
        AND IF YOU WANT TO OVERLOAD * THEN YOU HAVE TO USE __mul__
        For more info checkout: https://docs.python.org/3/reference/datamodel.html
'''
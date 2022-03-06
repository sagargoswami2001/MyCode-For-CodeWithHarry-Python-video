import os

a = None

if(a is None): # is - return true when variable a points to same object as specified in condition
    print("yes")
else:
    print("No")
    
'''
Q - Difference between == and is operator in Python?
Ans.The Equality operator (==) compares the values of both the operands and checks for value equality. 
    Whereas the 'is' operator checks whether both the operands refer to the same object or not 
    (present in the same memory location).                                              -geeksforgeeks

'''
    
    
a = [45,69,36,78]

# in return true when value is in specified List

print(67 in a)

a = (45,69,36,78)

# in return true when value is in specified tuple

print(67 in a)
    



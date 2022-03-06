import os

##if-elif-else ladder
a = 64
#in python indent is used to specify block of code, generally indent is either 4 spaces or 1 tab character
if(a>10): #Remember to use colon after each conditional statement
    print("a is Greater than 10")
elif(a>25): #elif is short for Else if
    print("a is Greater than 25 ")
else:
    print("a is not Greater than either 10 or 25")
    
a = 2

#if-else

if(a<0): 
    print("a is less than 0")
else: 
    print("a is greater than 0 ")


##Multiple if statements
a = 64

if(a>10): #if statement 1
    print("a is Greater than 10")
    
if(a>25): #if statement 2
    print("a is Greater than 25 ")
else:
    print("a is not Greater than either 10 or 25")

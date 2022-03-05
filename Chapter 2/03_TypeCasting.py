import os
a = 55 #int variable
print(type(a))
print("a is now ", a+45)

a = "55" # string variable due to double Quotes around no.
print(type(a), "\n")

a = int(a) # Typecasting String a into int a because string is a no and can be converted to int (if Possible)
print(type(a))
print("A is currently a integer ", a, "\n")

print("a is now a int so it can be Mathematically Treated: ", a+45)

a = str(a)  # Typecasting int into string
print(type(a))
print("A is currently a string " + a, "\n") #Here + Sign indicates string Concatination it can only be used for Strings

a = float(a)    # Typecasting String a into Float a because string is a no and can be converted to Float
print(type(a))
print("A is currently a Float ",  a, "\n")



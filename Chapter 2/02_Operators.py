import os
a = 55
b = 45


#Arithmatic Operation
print("a+b =", a+b) #Summation
print("a-b =", a-b) #Subtraction
print("a*b =", a*b) #Multiplication
print("a/b =", a/b) #division Note Division always Results in Floating Point value 
print("a%b =", a%b) #Modulus

print("\n")

#Assignment Operator
a = 46
print("a = ",a)
a += 5  # Actually means a = a + 5
print("a + 5 = ",a)
a -= 9  # Actually means a = a - 9
print("a - 9 = ",a)
a *= 2  # Actually means a = a * 5
print("a * 5 = ",a)
a /= 5  # Actually means a = a / 5
print("a / 5 = ",a)

print("\n")

#Comparison Operator
z = (a>b)   # is a Greater than b
print(z)
y = (a<b)   # is a Less then b
print(y)
z = (a>=b)  # is a Greater than or Equal to
print(z)
y = (a<=b)  # is a Less than or Equal to 
print(y)
z = (a==b)  # is a Equals to b
print(z)
y = (a!=b)  # is a Not Equal to b
print(y)

print("\n")

#Logical Operators
Bool1 = True
Bool2 = False

print("The Value Of Bool1 And Bool2 is: ", (Bool1 and Bool2)) #Prints True when both Bool1 and Bool2 are true
print("The Value Of Bool1 Or Bool2 is: ", (Bool1 or Bool2))   #Prints True when Either Bool1 and Bool2 are true
print("The Value Of Not Bool1 is: ", (not Bool1))   #Print True if Bool 1 is False, Prints False if Bool 1 is true
print("The Value Of Not Bool2 is: ", (not Bool2))   #Print True if Bool 2 is False, Prints False if Bool 2 is true




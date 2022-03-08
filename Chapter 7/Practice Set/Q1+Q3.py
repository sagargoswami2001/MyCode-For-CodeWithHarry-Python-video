#Practice set Q1 & Q3

# A Prorgram to print a multiplication table in Python
#Author: Prakash

import os 

no = int(input("Enter a no. to print it's multiplication table: ")) #Getting a no. from user and casting to int
multiplier = 1 #count


# using for loop with range 
for i in range(1, 11):
    print(no, "X", i, "=", no*i, '\n')
    
    

for i in range(1, 11):
#Easy method using fstrings 
    print(f"{no}X{i} = {no*i}")

print('\n')

#Practice set Q3
#using While-loop
while (multiplier<=10): 
    print(no, "X", multiplier, "=", no*multiplier, '\n')
    multiplier += 1
    





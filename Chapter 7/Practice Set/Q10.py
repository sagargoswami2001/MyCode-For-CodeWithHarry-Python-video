#Practice set Q2
#A Prorgram to print a multiplication table in Python in reverse order
#Author: Prakash

import os 

no = int(input("Enter a no. to print it's multiplication table: ")) #Getting a no. from user and casting to int

for i in range(10, 0, -1): #It is possible to let the range start at another number, 
                            #or to specify a different increment (even negative; sometimes this is called the ‘step’):

    print(f"{no}X{i} = {no*i}")
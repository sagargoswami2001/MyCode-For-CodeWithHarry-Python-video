# A Prorgram to demostrate range function with start, stop and step-size in Python
#Author: Prakash

'''
We can generate a sequence of numbers using range() function. 
range(10) will generate numbers from 0 to 9 (10 numbers)(till (n-1)).
'''

import os 

print("Welcome!")

for i in (range(10)): #Print form 0 to n-1 in this case 0-9
    print(i)

print('\n')
'''
We can also define the start, stop and step size as range(start, stop,step_size). 
Step size is generally not used much
step_size defaults to 1 if not provided.
'''

#Start and stop in range example
for i in (range(1, 10)): #Print form 1 to n-1 in this case 1-9
                        #Start and Stop is given in range function.
    print(i)

print('\n')

#same as above can be used to start from 2-10

for i in (range(2, 10)): #Print form 2 to n-1 in this case 2-9
                        #Start and Stop is given in range function.
    print(i)
    
print('\n')


#Start and stop and step-size in range example
for i in (range(1, 10, 2)): #Print form 1 to n-1 with skipping every other no.
                        #Start and Stop and step-size is given in range function.
    print(i)
    
print('\n')

for i in (range(1, 10, 3)): #Print form 1 to n-1 with skipping 2 no. after evry no.
                        #Start and Stop and step-size is given in range function.
    print(i)



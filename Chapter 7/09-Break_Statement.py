# A Prorgram to show for break statement in Python
#Author: Prakash

import os 

print("Welcome!")

for i in range(10): #This loop keeps iterating till condition become false and one condition is false else clause is executed
    print(i)
    if (i == 5):
        break #Break statement is used to break out of loop meaning to exit the loop then and there and discard the remaining iteration 
else: # This is Optionl part
    print('-1')
    
#else clause isn't executed since loop reached break and exited loop before condition became false, 
#else will only execute when loop is sucessfully terminated.
#due to break sucessfull termination isn't happening and loop is exited out midway


    


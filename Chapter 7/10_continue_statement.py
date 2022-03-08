# A Prorgram to show for continue statement in Python
#Author: Prakash

import os 

print("Welcome!")

for i in range(10): #This loop keeps iterating till condition become false and one condition is false else clause is executed
    if (i == 5):
        continue #continue statement is used to skip the current iteration of a loop and continue from next iteration.
    print(i)
    
else: # This is Optionl part
    print('-1')
    
#else clause will be executed since loop reached continue and skip that iteration but continues from next iteration
#till condition became false,
# 
#one condition become false else will be execute.

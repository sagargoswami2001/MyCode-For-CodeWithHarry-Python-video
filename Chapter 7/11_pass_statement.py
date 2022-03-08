# A Prorgram to show pass statement in Python
#Author: Prakash

import os 

print("Welcome!")

i = 1

# if (i>0): #if a for loop does nothing and have no body then it is an error if you want the for loop to not do anything
            #pass statement can be used as shown below.
            
if (i>0):   
    pass    #Doesn't do anything but isn't counted as an error
            #act as a null statement
            #pass can also be used with while loop
            
while(i>0):
    pass

for i in range(10):
    pass
print("Done.")


def sum(a, b): #Function can also use pass, function aren't covered yet and will be covered later
    pass
# A Prorgram to print contents of a list using while loop in Python
#Author: Prakash

import os 

aList = [1,2,4,6,3,5,8]

# Syntax of for Loop
# for val in sequence:  #val is the variable that takes the value of the item inside the sequence on each iteration.
                        #Loop continues until we reach the last item in the sequence. 
                        #The body of for loop is separated from the rest of the code 
                        # using indentation.
#     loop body

for item in aList: # for loop Doesn't require an explicitly defined variable to track loop
    print(item)


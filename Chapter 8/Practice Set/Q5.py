# #Practice set Q5
#Author: Prakash

import os 

n = 3
for i in range(n): #You can use the range function, but step using -1 to walk from n to 0.   
    print('*' * (n-i))#You can also make a string by multiplying a character by an integer. i starts with 0
                        #so in each row the columns will be same as rows, try changing value of n to see.
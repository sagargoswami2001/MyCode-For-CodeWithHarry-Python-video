# # #Practice set Q4
#Author: Prakash

import os 

def natural_sum_n(num):
    if num == 1 or num ==0:
        return 1

    sum = num + natural_sum_n(num-1)
    return sum


num = int(input("Enter the no of first natural no. you want to sum: "))
natural_sum_n(num)

print ("sum of first natural " + str(num) +  " numbers is " + str(natural_sum_n(num)))



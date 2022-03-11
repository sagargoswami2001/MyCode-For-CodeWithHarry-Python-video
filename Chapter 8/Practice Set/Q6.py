#Practice set Q6
#Author: Prakash

import os 

def inch_to_cms(inch):
    cms = inch*2.54
    return cms

inch = int(input("Enter length in inches: "))
cm = round(inch_to_cms(inch), 2)

print(f"{inch}inches is {cm}cms")

'''
Formula for converting inch to cms.
    cms = (inch × 2.54)

'''
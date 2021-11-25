#Solution of Practice Set Q7   

import os

FavLanguage = {}

a = input("Enter Your language Akash:")
b = input("Enter Your language Sagar:")
c = input("Enter Your language Kirti:")
d = input("Enter Your language Akash:")

FavLanguage["Akash"]=a # assigning inputs to specific keys
FavLanguage["Sagar"]=b
FavLanguage["Kirti"]=c
FavLanguage["Akash"]=d #if two key are same then latest input value is used for the key

print(FavLanguage)
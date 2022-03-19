# Practice set Q3
#Author: Prakash

import os 

class Whatever:
    a = "a = 1"
    
    def printAttribute(self):
        print(f"Que. Does Instance attribute changes class attribute?\nAns. No, it does not!\nclass attribute = {Whatever.a}.\ninstance attribute = {self.a} ")
    
lol = Whatever()
lol.a = "lol Instance attribute a = 0"

# Whatever.a = "This changes the class attribute"

# print(Whatever.a)
lol.printAttribute()



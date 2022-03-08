#Practice set Q2
#Author: Prakash

import os 

l1 = ["Prakash", "Sagar", "Deepak", "Akash", "Prince"]

for name in l1:
    if (name.startswith("P")): #for startswith is a function of list
        print(f"Hello {name}, Have a good day.")
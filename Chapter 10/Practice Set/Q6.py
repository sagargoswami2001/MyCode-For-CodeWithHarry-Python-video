# Practice set Q6
#Author: Prakash

import os 

class Sample:
    def __init__(slf, name): #Yes Self can  be rteplaced by another name but isn't recommended at all
        slf.name = name     #Whatever you will replace self with should be used for accessing instance attributes
        
obj = Sample("Zaphkill")
print(obj.name)
    

#Practice set Q1
#Author: Prakash

import os 

class C2DVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return (f"{self.icap}i + {self.jcap}j.")
    
            
'''
The __str__ method in Python represents the class objects as a string, it can be used for classes. The __str__ method
should be defined in a way that is easy to read and outputs all the members of the class.
'''


class C3dVector(C2DVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)    
        self.kcap = k
        
    def __str__(self):
        return (f"{self.icap}i + {self.jcap}j + {self.kcap}k.")

V2 = C2DVector(4, 8)
        
V3 = C3dVector(3, 4, 5)

print(V2)
print(V3)
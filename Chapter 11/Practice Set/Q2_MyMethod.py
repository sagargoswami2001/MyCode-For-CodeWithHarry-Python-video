#Practice set Q2
#Author: Prakash
#This is a Multilevel Inheritance

import os 

class Animals:
    AnimalType = "Mammal"

class Pets(Animals):
    Color = "White"

class Dogs(Pets):
    
    def bark(self, barksound):
        self.bark = barksound
    
    def __str__(self):
        return (self.bark)
        
D1 = Dogs()
D1.bark("WOOF!")
print(D1)


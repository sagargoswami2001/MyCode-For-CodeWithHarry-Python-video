#Practice set Q2
#Author: Prakash
#This is a Multilevel Inheritance

import os 

class Animals:
    AnimalType = "Mammal"

class Pets(Animals):
    Color = "White"

class Dogs(Pets):
    
    @staticmethod
    def bark():
        print("woof!")
        
D1 = Dogs()
D1.bark()
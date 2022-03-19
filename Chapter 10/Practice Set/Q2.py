# Practice set Q2
#Author: Prakash

from math import sqrt
import os 

class Claculator:
    
    def __init__(self, num):
        self.num = num
        
    def square(self):
        print(f"Square of given {self.num} is {self.num**2}.") 
        # '**' is Exponentiation oprator in python. ex. self.num**2 = (self.num)²  
        
    def cube(self):
        print(f"cube of given {self.num} is {self.num**3}.")
        # '**' is Exponentiation oprator in python. ex. self.num**3 = (self.num)³  
        
    def squreroot(self):
        print(f"sqroot of given {self.num} is {round(self.num**(0.5), 3)}.")
        # '**' is Exponentiation oprator in python. ex. self.num**0.5 = (self.num)⁽¹/²⁾  

num1 = Claculator(8)
num1.square()
num1.cube()
num1.squreroot()
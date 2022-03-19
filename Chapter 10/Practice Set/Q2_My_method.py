# Practice set Q2
#Author: Prakash

from math import sqrt
import os 

class Claculator:
    
    @staticmethod
    def square(no):
        sqr = (no*no)
        print(f"Square of given {no} is {sqr}.")
    
    @staticmethod
    def cube(no):
        cub = (no*no*no)
        print(f"cube of given {no} is {cub}.")
        
    @staticmethod
    def squreroot(no):
        sqroot = sqrt(no)
        print(f"sqroot of given {no} is {round(sqroot, 3)}.")
        
num1 = Claculator()
newNum = 8
num1.square(newNum)
num1.cube(newNum)
num1.squreroot(newNum)



#Practice set Q4
#Author: Prakash

import os 

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.image = i
        
    def __add__(self, c):
        print("Let's Add")
        return Complex(self.real + c.real, self.image + c.image)
    
    def __str__(self):
        if self.image<0:
            return f"{self.real} - {-self.image}i"
        else:
            return f"{self.real} + {self.image}i"
    
    def __mul__(self, c):
        print("Let's Multiply")
        mulReal = self.real * c.real - self.image * c.image
        mulImage = self.real * c.image + self.image * c.real
        return Complex(mulReal, mulImage)
    
    
n1 = Complex(3, 2)
n2 = Complex(1, 7)

print(n1 + n2)
print(n1 * n2)
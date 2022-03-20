import os 

class Number():
    def __init__(self, num):
        self.num = num
        
    def __add__(self, num2): 
        print("Let's Add")  
        return self.num + num2.num 
    
    def __mul__(self, num2):
        print("Let's Multiply")
        return self.num * num2.num

    def __str__(self): #This dunder Method is use to set what get shown when calling str(obj)/printing directly object
        return f"Decimal number {self.num}"
    
    def __len__(self):  #This dunder Method is use to set The length (obj)
        return 1

n1 = Number(4)
print(n1)

print(len(n1))
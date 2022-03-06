import os 

age = int(input("Enter Your age: "))

if (age == 18):
    print("Good, you can join from monday")
elif(age >=18 and age<=60):
    print("You can work here")
elif(age <18 or age>60):
    print("You are either too old or too young")
    
if (age>18 and age!=18):
    print("You are an adult")
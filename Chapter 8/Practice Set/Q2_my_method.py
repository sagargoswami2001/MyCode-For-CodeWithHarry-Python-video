#Practice set Q2
#Author: Prakash

import os 

def cel_to_fah(celcius):
    fahrenheit = (celcius*9/5)+32
    return fahrenheit

cel = int(input("Enter Temperature in Celcius: "))
fah = round(cel_to_fah(cel), 2)

print(f"{cel}°C is {fah}°F")

'''
Formula for converting celcius to fahrenheit.
    °F = (°C × 9/5) + 32
    
Formula for converting fahrenheit to celcius.
    °C = (°F − 32) x 5/9

'''

import os

Greet = "GoodMorning,"
Name = "Prakash"

#String Concatenation
print(Greet + Name) #'+' Operator Concatenates Strings

print(Greet[0])
print(Greet[1])
print(Greet[2])
print(Greet[3]) #Prints The Letter that is on 4th Place in (Char Array = String)

#print(Greet[13]) #Out of Range of char Array or String

#Greet[2] = 'S' #String object does not support item assignment

print("\n", Name[0:5])  #This Print a Part(Sliced Part) of String Of Given (Last Index -1) 
                        #First Value is Starting Index
print("\n", Name[1:5])

# Both Index Value are optional in String Slicing
print("\n", Name[:5]) #if First Index value is not given it is assumed to be 0 so its Same as Name[0:5]
print("\n", Name[0:]) #if Last Index value is not given it is assumed to be Last index of String so its Same as Name[0:6]
print("\n", Name[1:])

#Negative Index Works Like This 
# String =  P  r  a  k  a  s  h
# +Index =  0  1  2  3  4  5  6
# -Index = -7 -6 -5 -4 -3 -2 -1

print(Name[-7:-1])  # it is same as Name[0:6](Check in above table)

# slicinging With  Skiping

print(Greet[0:13:2])# it print a sliced String while skipping every 2nd Value in String 
            #last Argument in [] specify to skip value after every value of last argument
            
print(Greet[0:13:3]) #Here every 2 values will be skipped Like G then 2 values'oo' skipped and d is Printed
                    





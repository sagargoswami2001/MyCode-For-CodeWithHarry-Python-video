import os

#Creating a Tuples uses (), even if tuple have 1 value it needs an extra Comma
t1 = (5,) #Tuple with single element, if comma is not used it would not recognize it as tuple
# t1 = (5) #Wrong way to declare Tuple with single element
print(t1)

t2 = () #Empty Tuple

t = (0,8,6,9,4,'A')#This is a Tuple, Tuples can't be updated, it can hold data of Multiple Datatypes
print(t) # we can print tuple by tuple's name

print(t[0]) #you can print individual values by Specifying Their Index, Index starts at 0
print(t[2]) #if Index value is out of Range it will throw an error in this case a[7] would be out of range 
print(t[5])

# t[0]=5 #IT will Throw an Error as tuple can't be updated


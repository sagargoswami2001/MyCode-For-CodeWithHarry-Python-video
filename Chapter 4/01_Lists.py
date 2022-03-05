import os 
#Creating a Lists uses []
a = [45, 945, 77.69, 9, False, 7, 'apple'] #This is a List, It is a container that can hold multiple data of Different Datatype
#Lists can Contain Repeated Values
print(a) # we can print whole list by list's name

print(a[0]) #you can print individual values by Specifying Their Index, Index starts at 0
print(a[2]) #if Index value is out of Range it will throw an error in this case a[7] would be out of range 
print(a[4])
print(a[6])

#a[7] = 44 # new value can't be added 
# print(a[7]) # Will Throw an Error

a[1] = 87 # value in List can be overwritten
print(a[1])


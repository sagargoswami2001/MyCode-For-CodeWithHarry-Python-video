import os

#Set are unordered and unindexed and Can't be changed
a = {1,2,3,4,5,5,4,3,2,1}

#### To add elements in Set
a.add(2) #this statement doesn't do anything as elements can't be repeated, Repeating Value doesn't affect Set 
a.add(6) #adding Elements in Set one at a time at the front or 0 index

a.add((7,8,9,10)) # Tuple can be added to sets  

# a.add([7,8,9,10])# List can't be added in sets because lists can be modified afterwards
# a.add({0:11})# dict can't be added in sets because Dict can be modified afterwards

# Basically Data that isn't Hashable can be added to sets Meaning that if a data can be modified 
# after Creation Then it is not Hashable


print(a)

#### To find how many elements are in Set
print(len(a)) #return The No. of elements in a set

#### removes element from set
a.remove(5) # Removes all Occurence of 5 in Set 
# NOTE: If a value is repeated through tuple than it is not affected by remove
print(a)
# a.remove(15) #Throws an error because 15 isn't in set

#### removes any arbitrary(मनमाना) element from set
'''The pop() is an inbuilt method in Python that is used to pop out or 
remove the elements one by one from the set. The element that is the smallest 
in the set is removed first followed by removing elements in increasing order.'''
print(a.pop()) #removes any element from set a
print(a)

####Empties the Set
print(a.clear())


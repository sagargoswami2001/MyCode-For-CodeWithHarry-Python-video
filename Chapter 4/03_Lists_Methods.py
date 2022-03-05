import os

a = [45, 945, 77, 9, 84, 7, 6]


print(a) #prints the original list

#a1 = a.sort() # This is wrong Because sort Function sort the original list instead of returning sorted list


a.sort() #Sorts the Original List a 
print(a) #prints Sorted List


a.reverse() #Reverese the sorted(because original list got overwritten by sorted List) List a
print(a) #prints reversed List


# Definition of append from the Cambridge Advanced Learner's Dictionary & Thesaurus © Cambridge University Press
# append(verb) - to add something to the end of a piece of writing 

a.append(98) #Appends 98 to the end of the Reversed list
a.append(21)
print(a) #prints appended List

a.insert(2,65) #Inserts 65 at index 2 in appended List a 
#syntax: listname.insert(index, value)
print(a) #prints list with new element added at index 2 List

a.pop(5)#pops out whatever value is at index 5 in new inserted list
print(a) #prints list with poped out element at index 5

a.remove(945) #finds and Removes the element value 945
print(a) #prints List after removing 945 value





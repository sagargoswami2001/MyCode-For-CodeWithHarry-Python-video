##Practice set Q7
#Author: Prakash

import os 

'''
The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

Syntax
string.strip(characters)

Parameter  | Values	Description
characters | Optional. A set of characters to remove as leading/trailing characters

'''

# txt = ",,,,,rrttgg.....Anaconda....rrr"

# x = txt.strip(",.grt") #Characters to remove 

# print(x)

# txt = ",,,,,rrttgg.....Anaconda....rrr"

# x = txt.strip("") #No characters to remove means remove spaces 

# print(x)

def remove_and_strip(stri, word ):
    newstr = stri.replace(word, "")   
    return newstr.strip()
    
stri = "What in the word"
    
n = remove_and_strip(stri, "word")

print(n)

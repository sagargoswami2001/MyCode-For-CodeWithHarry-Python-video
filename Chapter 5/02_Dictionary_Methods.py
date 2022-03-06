import os 

myDict = {
            "hungry" : "Due to fast metabolism",# Key can be Lower case or Upper case 
            "Flash": "Fastest Man Alive",
            "Age": 24,
            "Other Members": ["Superman", "WonderWoman", "Batman"], # Lists can also be defined inside dict 
            
            "Teen Titans" : ("Cyborg", "Star fire, raven, Beastboy, Robin"),     #Dictionaries Can Contain Tuples too
            
            "Co-op Team" : {"Nightwing":"All Rounder Leader", 
                            "Aquaman":"Vice Leader",
                            "Superboy":"Heavy Hitter",
                            "Miss Martian": "Psychic Force"}, #We can also Define a Dict under Another Dict meaning Nesting of Dict is possible
            1:(1.0) #This is a Tuple containing a floating point no. 
}#Remember to use, after each entry

print("\n\n", myDict.keys())         #Prints all the keys in List Fashion
print("\n\n", type(myDict.keys()))   #prints the Type of dict
print("\n\n", list(myDict.keys()))   #Typecasting Dict to List
print("\n\n", myDict.values(), "\n")       #Prints all the values in Dict in List Fashion
print("\n\n", myDict.items())        #Prints dict Contents as a tuple(key, values) for all values

print("\n\n",myDict, "\n")
updatedDict={
    "New Members": ["Martian Manhunter", "Atom", "Shazam"], 
    1:2 #This is a Tuple containing a integer no. 
    }# Dictionaries can be updated and we can add new keys and values pairs in our previous dict
    #Predifined Key and Values can also be Overwritten in this manner
    
myDict.update(updatedDict) # Updating dictionaries

print("\n\n",myDict) #Printing new Dictionary

print(myDict.get("Flash")) # Prints value associated with key "Flash"
print(myDict["Flash"]) # Prints value associated with key "Flash"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("Flashs2")) # Returns None as Flash2 is not present in the dictionary
#print(myDict["Flashs2"]) # throws an error as Flash2 is not present in the dictionary

#NOTE: More methods can be found on Python Docs: https://docs.python.org/3/library/stdtypes.html#dict

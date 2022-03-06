import os 
# Dictionaries are Unordered
# Dictionaries can't contain duplicate Keys, if key is redifined then it is overwritten by Latest Definition
myDict = {
            "Hungry" : "Due to fast metabolism",
            "Flash": "Fastest Man Alive",
            "Age": 24,
            "Other Members": ["Superman", "WonderWoman", "Batman"], # Lists can also be defined inside dict
            
            "Teen Titans" : ("Cyborg", "Star fire, raven, Beastboy, Robin"),     #Dictionaries Can Contain Tuples too

            "Co-op Team" : {    "Nightwing":"All Rounder Leader", 
                                "Aqualad":"Vice Leader",
                                "Superboy":"Heavy Hitter",
                                "Miss Martian": "Psychic Force"     
                            } 
            #We can also Define a Dict under Another Dict meaning Nesting of Dict is possible
}           # Remember to use, after each entry

print(myDict["Flash"])  # use [] for printing Entries from Dict
print(myDict["Hungry"])
print(myDict["Age"])

myDict["Other Members"] = ["Superman", "Wonder Woman", "Batman", "Green Lantern"]
# Dictionaries can be changed/Modified(mutable)


print(myDict["Other Members"])# Printing Updated List From Dictionary 

print(myDict["Co-op Team"]["Nightwing"])
#printing Nested Dictionary the elements of Nested Dictionary can be accessed by a 2nd []






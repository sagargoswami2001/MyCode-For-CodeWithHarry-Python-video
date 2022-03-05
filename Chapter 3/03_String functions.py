import os


Dialogue = "on that day, everything changed! catestrophic destruction Became Child's Play"

print(len(Dialogue)) #Prints the Length of a string 


print(Dialogue.endswith("Play")) #print true if a given String end match with given Keyword

print(Dialogue.count("a")) #Prints the No. of time a char or substring appears in a string 
print(Dialogue.count("On"))

print(Dialogue.capitalize()) # Capitalize First Letter of a string 

print(Dialogue.find("Became")) # Find and Return Location of a string, 
                                #if Multiple match is found them Location of First Match is Returned
print(Dialogue.find("bagdad")) # Returns -1 if String not found

print(Dialogue.replace("on", "in")) #Replace all Matching Occurences
print(Dialogue.replace("day", "Time"))  
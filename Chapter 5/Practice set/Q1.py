#Solution of Practice Set Q1

import os

HindiDict = {
    "Kya":"What",
    "Nhi":"No",
    "Ha": "Yes" 
}
print("Option are:", HindiDict.keys())
a = input("Enter Hindi Word to find it's english meaning: ")

print(a,"means: ", HindiDict.get(a))

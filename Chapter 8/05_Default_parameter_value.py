# A Prorgram to show default parameters in Python
#Author: Prakash

import os 

def namePrinter(fName, sName = "Tokisaki"): # Here parameter sName already have a default value
                                            # it will be used in case a Sname argument isn't passed, but passing fname is mandetory
    print(f"Name is {fName} {sName}")
    
fName = "Kurumi"
sName = "Tokisaki"

namePrinter(fName, sName)# Both argument is passed
print('\n')
namePrinter(fName)  # only fName argument is passed in this case dafault parameter value will be used
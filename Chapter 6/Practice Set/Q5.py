#Solution of Practice Set Q5
import os 

Name_List = ["Prakash", "Kirti", "Sagar"]
Name_to_find = input("Enter name to search in list: ")

if(Name_to_find in Name_List):
    print("Name is Present in List ")
else:
    print("Name isn't Present in List ")
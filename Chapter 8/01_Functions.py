# A Prorgram to demonstrate functions in Python
#Author: Prakash
import os 

marks = [14,26,16,21] #Marks from 30
marks2 = [18,24,26,13] #Marks from 30
'''
a function is a group of related statements that performs a specific task.
Functions help break our program into smaller and modular chunks. 
As our program grows larger and larger, functions make it more organized and manageable, 
a function can be called(used) any numbers of times.
'''

#The def keyword is used to create, (or define) a function.
def percentage(alist): #Functions can take any no of parameters inside (), although it's optional
    #The information received by called function are known as parameters.
    #A function can return data as a result, here we are returning percentage to caller
    
    percent = ((alist[0] + alist[1] + alist[2] + alist[3])/120)*100  #--|
    return percent  #---------------------------------------------------|->these line are known as function definition


mPercentage = round(percentage(marks), 2) #calling percentage function and storing the returned value in marksPercentage
                                        #Information can be passed into functions as arguments.
                                        # Arguments are specified after the function name, inside the parentheses. 
                                        # You can add as many arguments as you want, just separate them with a comma.
                                        #The information passed by caller are called arguments
print(f"The percenrtage of given marks is: {mPercentage} ")


mPercentage = round(percentage(marks2), 2)
print(f"The percenrtage of given marks2 is: {mPercentage} ")








#Python program to Open and write into file
#Author: Prakash

import os 

#opening Empty file in write mode

# FOR USER TO DO : (Check if it is empty if not, then delete it's content)

f = open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//03_Writing_in_files//sample1.txt", 'w')
#if file wasn't already there then it will be made

#f.write("Whatever")

f.write(" Whatever, Previous line will be overwritten by this line") #write function will overwrite the whole file

#for appending we can open the file in append mode

f.close()
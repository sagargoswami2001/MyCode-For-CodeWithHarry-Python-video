#Python program to Open and appending into file
#Author: Prakash

import os 

#opening Empty file in write mode
#sample1.txt already have contents

f = open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//04_Appendig _files//sample1.txt", 'a')

f.write(", Appending this in file") #write function will append instead of overwriting the whole file
#if file is ran multiple times it will be appended for each run 


f.close()
#Python program to Open and Read a file using open() function
#Author: Prakash

import os 
'''
Files are named locations on disk to store related information. 
They are used to permanently store data in a non-volatile memory (e.g. hard disk).

Since Random Access Memory (RAM) is volatile 
(which loses its data when the computer is turned off), 
we use files for future use of the data by permanently storing them.

Python has a built-in open() function to open a file. This function returns a file object, 
it is used to read or modify the file accordingly.

We can specify the mode while opening a file. In mode, we specify whether we want to read r, 
write w or append a to the file. We can also specify if we want to open the file in text mode or binary mode.

The default is reading in text mode. In this mode, we get strings when reading from the file.
On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files 
like images or executable files.
'''

#Replace the file path with Your File path
#f = open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//01_File//sample.txt", 'r') 
f = open("D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//01_File//sample.txt") #No 'r' specified
# Opening a file in Read mode Which is Default mode(Can be omitted if you like), sample.txt must be in same directory 
# where you are runing code or You will have to manually Specify the directory as i have


#data = f.read() 
#Reading the contents of file in a variable data 
data = f.read(7) #You can also specify how many characters to read from file. as argument in read() 
#once you read from file then you can't read again 

print(data)

#After we are done, we should ALWAYS close the file
#Closing a file will free up the resources that were tied with the file. It is done using the close() function
f.close()


'''
NOTE:   In windows You might get an error while reading file using normal path as windows use '\' in path
        Replace all '\' in windows path with '//' as i have done 
'''


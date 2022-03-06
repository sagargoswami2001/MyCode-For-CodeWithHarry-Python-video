#Solution of Practice Set Q2
import os 

Marks1 = int(input("Enter Marks of Subject 1: "))
Marks2 = int(input("Enter Marks of Subject 2: "))
Marks3 = int(input("Enter Marks of Subject 3: "))
    
Total_Percentage = float(((Marks1+Marks2+Marks3)/300)*100)
Total_Percentage = round(Total_Percentage, 3)#rounding fraction to reduce precision

if(Marks1<33 or Marks2<33 or Marks3<33): #In one of the subject you have less then 33 marks
    print("You FAILED!")    
elif(Total_Percentage<40): #Your Total Percentage is less than that of 40%
    print("You are FAILED!")
elif(Total_Percentage>100): #Someone Needs to be fired!
    print("Oops, There has been some mistake!")
else:   #You pass, Somehow.
    print("Congratulations, You are Pass. You've got ", Total_Percentage,"%")
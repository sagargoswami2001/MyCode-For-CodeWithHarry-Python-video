import os 

Marks1 = int(input("Enter Marks of Subject 1: "))
Marks2 = int(input("Enter Marks of Subject 2: "))
Marks3 = int(input("Enter Marks of Subject 3: "))
    
Total_Percentage = float(((Marks1+Marks2+Marks3)/300)*100)
Total_Percentage = round(Total_Percentage, 3)

if(Marks1<33 or Marks2<33 or Marks3<33):
    print("You FAILED!")    
elif(Total_Percentage<40):
    print("You are FAILED!")
elif(Total_Percentage>100):
    print("Oops, There has been some mistake!")
else:
    print("Congratulations, You are Pass. You've got ", Total_Percentage,"%")
#Solution of Practice Set Q6

import os 

Grade = int(input("Enter Your Grade: "))

if(Grade<50):
    print("ou got a Grade of 'F': Fail!")
elif(Grade>=50 and Grade<60):
    print("You got a Grade of 'D'")
elif(Grade>=60 and Grade<70):
    print("You got a Grade of 'C'")
elif(Grade>=70 and Grade<80):
    print("You got a Grade of 'B'")
elif(Grade>=80 and Grade<90):
    print("You got a Grade of 'A'")
elif(Grade>=90 and Grade==100):
    print("You got a Grade of 'Ex'")
else:
    print("Couldn't Determine your Grade")
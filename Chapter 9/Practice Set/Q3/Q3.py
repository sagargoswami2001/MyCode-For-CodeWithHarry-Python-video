#Practice set Q3
#Author: Prakash
import os 


for i in range(2, 21):
    with open(f"D://Users//Zaphkil!//Documents//VS Code//Python//Workspace//Chapter 9//Practice Set//Q3//tables//Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range (1, 11):
            f.write(f"{i} X {j} = {i*j}")
            if(j!=10):
                f.write('\n')
    #break
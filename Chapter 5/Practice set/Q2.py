#Solution of Practice Set Q2

import os

set = set() 

a = int(input("enter no.1:" ))
b = int(input("enter no.1:" ))
c = int(input("enter no.2:" ))
d = int(input("enter no.3:" ))
e = int(input("enter no.4:" ))
f = int(input("enter no.5:" ))
g = int(input("enter no.6:" ))
h = int(input("enter no.7:" ))

set.add(a)      #Adding no. in Set one by one
set.add(b)
set.add(c)
set.add(d)
set.add(e)
set.add(f)
set.add(g)
set.add(h)
        # OR
#another more direct Method
set1 = {a,b,c,d,e,f,g,h}

print(set)
print(set1)
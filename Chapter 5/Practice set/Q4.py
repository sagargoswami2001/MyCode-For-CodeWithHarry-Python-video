#Solution of Practice Set Q4
import os

S = set()
S.add(20)
S.add(20.0) #Int and Float are considred same thing for Same value meaning 20 = 20.0 in Sets
S.add("20")

print(len(S))
print(S)


import sys

v = sys.argv[1]

o = ["[","{","("] 
c = ["]","}",")"]

q = []

if len(v)==0:
    print("true")
    exit()
for i in v:
    if i in o:
        q.append(i)
    if i in c:
        if i == c[o.index(q[-1])]:
            q.pop()
        else:
            print("false")
            exit()
        
    
if len(q)==0:
    print("true")
else:
    print("false")

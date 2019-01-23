c = int(input())
v = list(map(int,input().split()))
o = v[0:3]
tr = v[3:]
def double_link():
    for i in range(2,len(tr),3):
        if tr[i]==o[0]:
            return
        else:
            o.append(tr[i])
        
double_link()
print(len(o))
print(*o)

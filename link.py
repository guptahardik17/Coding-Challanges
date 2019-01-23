c = int(input())
v = list(map(int,input().split()))
o = []
def link(o):
    temp = []
    for i in range(len(v)):
        if v[i]%2==0:
            temp.append(v[i])
        else:
            if len(temp)>0:
                o+=sorted(temp,reverse=True)
                temp = []
            o.append(v[i])
    if len(temp)>0:
        o+=sorted(temp,reverse=True)
        temp=0
    return o
o = link(o)
print(*o)

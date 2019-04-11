count = int(input())
v = list(map(int,input().split()))

l1 = []
l2 = []
parmanent = []
l = []
for i in range(count):
    for j in range(count-i):
        l1 = v[i:j+i+1]
        l2 = v[j+i+1:]
        l2+=parmanent
        
        av1 = sum(l1)/float(len(l1))
        
        if len(l2)==0:
            if av1>0:
                l.append([i+1,i+j+1])
        else:
            if av1>(sum(l2)/float(len(l2))):
                l.append([i+1,i+j+1])
        
    parmanent.append(v[i])
    
print(len(l))
for s in l:
    print(*s)
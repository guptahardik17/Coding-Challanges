t = int(input())

for i in range(t):
    c = int(input())
    v = list(map(int,input().split()))
    
    v = sorted(v,reverse=True)
    
    o = 0
    l = []
    for j in v:
        l.append(2*o+j)
        o+=j
        
    print(sum(l))

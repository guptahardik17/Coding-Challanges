c = int(input())
v = list(map(int,input().split()))
    
s = sum(v)    
l = [s-v[i] for i in range(c)]

print(min(l))

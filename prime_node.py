def prime(num):
    for i in range(2, int(num/2)):
    	if num % i  == 0:
    		return 0;
    		break
    else:
    	return 1;

c = int(input())
v = []
for i in range(c-1):
    v.append(list(map(int,input().split())))
    
p = {}
for i in range(0,c-1):
    if v[i][0] not in p:
        p[v[i][0]] = v[i][1]
    else:
        p[v[i][0]] = p[v[i][0]] + v[i][1]
count = 0
for i in p:
    l = prime(p[i])
    count+=l
    
print(count)

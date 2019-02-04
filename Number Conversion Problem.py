e_count = int(input())
elements = list(map(int,input().split()))
count = int(input())
for i in range(count):
    v = list(map(int,input().split()))
    
    if v[0]==1:
        elements[v[1]-1] = v[2]
    else:
        for j in range(v[1]-2,-1,-1):
            if elements[v[1]-1]!=elements[j]:
                break
        if j!=0:
            print(j+2)
        else:
            print(1)
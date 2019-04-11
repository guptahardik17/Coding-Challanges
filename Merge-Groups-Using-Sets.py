size = int(input())
inputs = list(map(int, input().split()))
l = [set([val]) for val in inputs]
count = int(input())

for x in range(count):
    value = list(map(int, input().split()))
    
    if value[0]==2:
        if len(l[value[1]-1])==1:
            print(0)
        else:
            print(abs(max(l[value[1]-1])-min(l[value[1]-1])))
    elif value[0]==1:
        if l[value[1]-1] == l[value[2]-1]:
            pass
        else:
            union = l[value[1]-1] | l[value[2]-1]
            l[value[1]-1],l[value[2]-1] = union,union
        
        
        
    
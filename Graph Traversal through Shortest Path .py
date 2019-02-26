t = int(input())

for i in range(t):
    n,e = input().split()
    l = []
    for j in range(int(e)):
        l.append(list(map(int,input().split())))
    start = int(input())
    covered = [start]
    output = []
    status = 1
    while(status==1):
        temp = [x for x in l if x[0] in covered or x[1] in covered]
        temp.sort(key=lambda x: x[2])
        # print(temp)
        bl = len(l)
        for k in temp:
            if k[1] not in covered:
                l.remove(k)
                covered.append(k[1])
                output.append(k[2])
                break
            if k[0] not in covered:
                l.remove(k)
                covered.append(k[0])
                output.append(k[2])
                break
        al = len(l)
        if bl==al:
            status = 0
    
    print(*output)
    
import sys
def graph(s,count):
    print(v[s])
    for k in v[s]:
        if k in v:
            graph(k,count+1)
        else:
            if count>nl[0]:
                del nl[:]
                nl.append(count)
                nl.append(k)


t = int(sys.stdin.readline())
for i in range(t):
    nl = [0]
    c = int(sys.stdin.readline())
    v = {}
    temp = []
    for j in range(c-1):
        x = list(map(int,sys.stdin.readline().split()))
        
        if x[0] in v:
            v[x[0]].append(x[1])
        else:
            v[x[0]] = [x[1]]
    s = int(sys.stdin.readline())
    graph(s,1)
    sys.stdout.write(str(nl[1])+"\n")
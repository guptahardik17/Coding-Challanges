t = int(input())

for x in range(t):
    count = int(input())
    graph = []
    for i in range(count):
        graph += [list(map(int, input().split()))]
    
    done = False
    for i in range(count):
        for j in range(count):
            if graph[i][i]!=0:
                done = True
                break
            if i!=j and (graph[i][j]!=graph[j][i] or graph[i][j]<=0 or graph[j][i]<=0):
                print(graph[i][j],graph[j][i])
                done = True
                break
            for k in range(count):
                if graph[j][i]+graph[i][k]<graph[j][k]:
                    done = True
                    break
            if done:
                break
        
        if done:
            break
    
    if done:
        print("NO")
    else:
        print("YES")
        
def schedule(tasks, viable_tasks=None):
    if not viable_tasks:
        viable_tasks = []
        tasks = sorted(tasks)
    found_viable = False
    for i, (start, end) in enumerate(tasks):
        for viable_start, viable_end in viable_tasks:
            if viable_start < start < viable_end or viable_start < end < viable_end or start < viable_start < end or start < viable_end < end:
                break
        else:
            found_viable = True
            yield from schedule(tasks[:i] + tasks[i + 1:], viable_tasks + [[start, end]])
    if not found_viable:
        yield viable_tasks

t = int(input())

for i in range(t):
    count = int(input())
    l = []
    for j in range(count):
        temp = []
        v = list(input().split())
        
        (h, m) = v[1].split(':')
        v[1] = int(h) * 3600 + int(m) * 60
        temp.append(v[1])
        
        (h, m) = v[2].split(':')
        v[2] = int(h) * 3600 + int(m) * 60
        temp.append(v[2])
        
        l.append(temp)
    # print(l)
    # l = sorted(l)
        
    # o = []
    # for j in range(0,int(count/2)):
    #     start = l[j][0]
    #     end = l[j][1]
    #     output = 1
        
    #     for k in range(j+1,count):
    #         if l[k][0]<end:
    #             pass
    #         else:
    #             end = l[k][1]
    #             output+=1
    #     o.append(output)
            
    # print(max(o))
    

    print(len(max(schedule(l), key=len)))

    
    # o = (l)
    # c = 0
    # for el in o:
    #     if len(el)>c:
    #         c = len(el)
            
    # print(c)
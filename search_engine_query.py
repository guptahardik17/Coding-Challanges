t = int(input())
for i in range(t):
    d = {}
    count = int(input())
    
    for j in range(count):
        value = input()
        if value[:3]=='top' and value[4].isdigit():
            splitted = value.split()
            sorted_d = sorted(d, key=lambda k: (-d[k], k))
            print(*sorted_d[:int(splitted[1])])
        else:
            if value not in d:
                d[value]=1
            else:
                d[value]+=1
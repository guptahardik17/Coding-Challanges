t = int(input())

for x in range(t):
    count = int(input())
    s1 = sorted(list(input().strip()))
    s2 = sorted(list(input().strip()))
    
    counter1 = 0
    counter2 = 0
    counter = 0
    while counter1!=count or counter1!=count:
        if s1[counter1]==s2[counter2]:
            counter+=1
            counter1+=1
            counter2+=1
        elif ord(s1[counter1])<ord(s2[counter2]):
            counter1+=1
        elif ord(s2[counter2])<ord(s1[counter1]):
            counter2+=1
            
    print(counter)

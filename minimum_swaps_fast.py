from sys import stdin

t = int(stdin.readline())

for x in range(t):
    count = int(stdin.readline())
    values = list(map(int,stdin.readline().split()))
    maximum = max(values)
    if count < 3:
        print(0)
    else:
        if count%2!=0:
            temp = int((count+1)/2)
            mid1,mid2 = temp,temp
        else:
            mid1,mid2 = int(count/2),int((count/2)+1)
            
        for i in range(mid1):
            if values[mid1-i-1]==maximum or values[mid2-1+i]==maximum:
                print(i)
                break
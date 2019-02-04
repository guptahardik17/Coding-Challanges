t = int(input())
for i in range(t):
    count = int(input())
    a = list(map(int,input().split()))
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    
    low = a[0]-q[0]
    high = a[0]+p[0]

    for j in range(1,count):
        if a[j]-q[j]>low:
            low = a[j]-q[j]
        if a[j]+p[j]<high:
            high = a[j]+p[j]
            
    print(high-low+1)
    
#     %reset -f
n,q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(q):
    l,r,p,k = map(int, input().split())
    bArr = arr[l-1:r]
    XR = 0
    for iterations in range(p):
        for index in range(r-l+1):
            XR = XR ^ (bArr[index] + k)
        bArr = [int(x / 2) for x in bArr]

    if(XR % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
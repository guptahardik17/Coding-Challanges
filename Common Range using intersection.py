def solve (n, A, P, Q):
    # l = []
    # for it in range(n):
    #     t1 = list(range(P[it]+1))
    #     t2 = list(range(Q[it]+1))
        
    #     t1 = list(map(lambda x:x+A[it], t1))
    #     t2 = list(map(lambda x:A[it]-x, t2))
    #     l.append(t1+t2)
        
        
    # result = set.intersection(*map(set, l))
    
    # return(len(result))
    
    
    low = A[0]-Q[0]
    high = A[0]+P[0]

    for j in range(1,n):
        if A[j]-Q[j]>low:
            low = A[j]-Q[j]
        if A[j]+P[j]<high:
            high = A[j]+P[j]
            
    return(high-low+1)

T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    out_ = solve(n, A, P, Q)
    print (out_)
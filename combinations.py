import math

def nCr(n,r):
    f = math.factorial
    return f(n+r-1) // f(r) // f(n-1)

t = int(input())
for i in range(t):
    n, k, m = map(int, input().split())
    print(nCr(n-k+1,m))
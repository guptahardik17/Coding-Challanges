N, X, Y, Z, T = map(int, input().split())
A = list(map(int, input().split()))

finalList = []

for i in range(X,Z+1):
    for j in range(Y,T+1):
        finalList.append(A[i-1] & A[j-1]);
        
finalValue = finalList[0] ^ finalList[1]
for fv in range(2, len(finalList)):
    finalValue ^= finalList[fv]
print(finalValue)
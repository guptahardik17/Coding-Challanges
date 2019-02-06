#- EQUAL DIVISION -#

t = int(raw_input())
b = []
n = []
status = 0
counter = 0
p = 0

for i in range(t):
    temp = map(int, raw_input().split())
    b.append(temp[0])
    n.append(temp[1])
    
def checkstatus():
    for i in range(t):
        if b[i]%n[i]==0 or n[i]%b[i]==0:
            status = 1
            p=0
        else:
            status = 0
            p = i
            if t-i>=2:
                r = max(b[i],n[i])/min(b[i],n[i])
                rn = max(b[i+1],n[i+1])/min(b[i+1],n[i+1])
                if r!=rn:
                    return status,p
            
    return status,p
    
status,p = checkstatus()
while status==0:
    for j in range(p+1):
        b[j]+=1
    counter+=1
    status,p = checkstatus()
print counter
#-- VEGETABLE MARKET --#

c = int(raw_input())
s = map(int, raw_input().split())
q = int(raw_input())
minimum = []
l = []

for i in range(q):
    minimum.append(int(raw_input()))


def find(i):
    if sum(s)<i:
        return -1
    elif sum(s)==i:
        return max(s)
    else:
        for j in range(max(s)+1):
            count=0
            for k in s:
                if k>=j:
                    count+=j
                if k<j:
                    count+=k
                if count>=i:
                    return j
    
for i in minimum:
    y = find(i)
    print y
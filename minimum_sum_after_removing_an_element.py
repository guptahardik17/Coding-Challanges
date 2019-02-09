t = int(input())

for i in range(t):
    c = int(input())
    v = list(map(int,input().split()))
    m_diff = 0
    m_val = 0
    sum = 0
    for j in range(c-1):
        temp = abs(v[j]-v[j+1])
        # print(temp)
        sum += temp
        if temp > m_diff:
            m_diff = temp
            m_val = max(v[j],v[j+1])
            
    position = v.index(m_val)
    if position == c-1 or position == 0:
        sum-=m_diff
    else:
        sum-= abs(v[position-1] - v[position])
        sum-= abs(v[position] - v[position+1])
        sum+= abs(v[position-1] - v[position+1])
    print(sum)
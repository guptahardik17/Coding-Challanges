t = int(input())

for i in range(t):
    count = int(input())
    values = list(map(int,input().split()))
    l = []
    mini = count
    if count < 3:
        print(0)
    else:
        if count%2!=0:
            mid = int((count+1)/2)
            m_val = max(values)
            if values[mid-1]==m_val:
                print(0)
            else:
                for j in range(count):
                    if m_val == values[j]:
                        if abs(mid-j-1)<mini:
                            mini = abs(mid-j-1)
                print(mini)
        else:
            mid1 = int(count/2)
            mid2 = int((count/2)+1)
            m_val = max(values)
            
            if values[mid1-1]==m_val or values[mid2-1]==m_val:
                print(0)
            else:
                for j in range(count):
                    if m_val == values[j]:
                        if abs(mid1-j-1)<mini:
                            mini = abs(mid1-j-1)
                        if abs(mid2-j-1)<mini:
                            mini = abs(mid2-j-1)
                print(mini)
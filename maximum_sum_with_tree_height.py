t = int(input())

for i in range(t):
    c = int(input())
    val = list(map(int,input().split()))
    height = list(map(int,input().split()))
    c_changer = int(input())
    index = list(map(int,input().split()))
    min_height = list(map(int,input().split()))
    m_height = 0
    s = 0
    indexer = 0
    for j in range(c):
        if j==index[indexer]:
            if min_height[indexer]<m_height:
                s+=val[j]
                if indexer != c_changer-1:
                    indexer+=1
            else:
                s = -1
                break
        else:
            if m_height==0:
                m_height+=height[j]
            else:
                s+=val[j]
        
        
    print(s)
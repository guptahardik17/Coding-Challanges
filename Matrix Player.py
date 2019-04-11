count = int(input())
limits = list(map(int,input().split()))
l,indexer,l1,l2,l3 = [],[],[],[],[]
output = []
for x in range(count):
    value = list(map(int,input().split()))
    l.append(value)
    m_val = max(value)
    
    if value[0]>=value[1] and value[0]>=value[2]:
        indexer.append(m_val)
        l1.append(m_val)
    elif value[1]>=value[0] and value[1]>=value[2]:
        indexer.append(m_val)
        l2.append(m_val)
    elif value[2]>=value[0] and value[2]>=value[1]:
        indexer.append(m_val)
        l3.append(m_val)
        
initial = limits.index(max(limits))

l1 = sorted(l1,reverse=True)
output = l1[:limits[0]]
new_l1 = l1[limits[0]:]

for i in new_l1:
    temp = indexer.index(i)
    if l[temp][1]>=l[temp][2]:
        l2.append(l[temp][1])
    else:
        l3.append(l[temp][2])
        
l2 = sorted(l2,reverse=True)
output += l2[:limits[1]]
new_l2 = l2[limits[1]:]

for i in new_l2:
    temp = indexer.index(i)
    l3.append(l[temp][2])

l3 = sorted(l3,reverse=True)
output += l3[:limits[2]]

print(sum(output))
        
#Processing l1 First
# l1 = sorted(l1,reverse=True)
# output = l1[:limits[0]]
# new_l1 = l1[limits[0]:]

# for i in new_l1:
#     temp = indexer.index(i)
#     if l[temp][1]>=l[temp][2]:
#         l2.append(l[temp][1])
#     else:
#         l3.append(l[temp][2])
        
# l2 = sorted(l2,reverse=True)
# output += l2[:limits[1]]
# new_l2 = l2[limits[1]:]

# for i in new_l2:
#     temp = indexer.index(i)
#     l3.append(l[temp][2])

# l3 = sorted(l3,reverse=True)
# output += l3[:limits[2]]

# print(sum(output))


#Processing l2 First

#Processing l2 First
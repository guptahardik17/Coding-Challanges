x = raw_input().split()
s = x[0]
e = x[1]
l = []
start = []
end = []
price = []


try:
	while True:
		l.append(raw_input().split())
except EOFError:
	pass

length = len(l)

for i in range(0,length):
    start.append(l[i][0])
    end.append(l[i][1])
    price.append(int(l[i][2]))

nl = []
sum = 0
ns = s
temp = []

for i in range(length):
    if s==start[i] and e==end[i]:
        sum+=price[i]
        temp.append(ns+" "+end[i])
        temp.append(sum)
        sum = 0
        s = x[0]
        e = x[1]
        ns = s
        nl.append(temp)
        temp = []
    elif s==start[i] and e!=end[i]:
        s = end[i]
        ns = ns +" "+ end[i]
        sum+=price[i]

if len(nl)==0:
    print "No Flights"

final_list = []
for i in nl: 
    if i not in final_list: 
        final_list.append(i) 
for i in range(len(nl)):    
    for j in range(i,len(nl)):
        if final_list[i][1] == final_list[j][1]:
            if len(final_list[i][0].split())>len(final_list[j][0].split()):
                c = final_list[i]
                final_list[i] = final_list[j]
                final_list[j] = c
                

fl = sorted(final_list, key = lambda x: x[1])

for i in range(len(fl)):
    print fl[i][0]+" "+str(fl[i][1])
t = int(input())
for x in range(t):
  n, b = input().split()
  n = int(n)
  b = b.split(',')
  l = []
  l.append(int(b[0][1:]))
  l.append(int(b[1][-2::-1]))
  
  output = n+n-2
  d1 = n-max(l)
  d2 = min(l)-1
  
  t1 = []
  t1.append(n-l[0])
  t1.append(l[1]-1)
  
  t2 = []
  t2.append(n-l[1])
  t2.append(l[0]-1)
  
  d3 = min(t1)
  d4 = min(t2)
  
  output = output+d1+d2+d3+d4
  print(n*n-output)
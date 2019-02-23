import sys

t = int(sys.stdin.readline())
for x in range(t):
  n, b = sys.stdin.readline().split()
  n = int(n)
  b = b.split(',')
  l = []
  l.append(int(b[0][1:]))
  l.append(int(b[1][-2::-1]))
  l.append(n-min(l))
  output = 3*(n-1)+2*(min(l)-1)
  sys.stdout.write(str(n*n-output)+'\n')
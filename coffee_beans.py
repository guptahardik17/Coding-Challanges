def beans(n,output):
    for j in range(c):
        for i in range(j,c):
          if n%values[i] == 0:
              output+=int(n/values[i])
              l.append(output)
          else:
              temp = int(n/values[i])
              output+=temp
              n = n - values[i]*temp



t = int(input())
for x in range(t):
  l = []
  output = 0
  n, c = map(int, input().split())
  values = sorted(list(map(int,input().split())), reverse=True)
  
  if values[-1]>n:
    print("NO")
  else:
    beans(n,output)
    if l:
        print(min(l))
    else:
        print("NO")
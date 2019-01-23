l = []
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if s == target:
        l.append(partial)
    if s >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        if len(l)>0:
            return
        subset_sum(remaining, target, partial + [n])

t = int(input())
for x in range(t):
  l = []
  v = list(map(int, input().split()))
  c = int(input())
  val = v[1:]
  n = v[0]
  
  s = sum(val)
  if s<c:
      print("NO")
  elif s==c:
      print("YES")
  else:
      subset_sum(val, c)
      if len(l)>0:
          print("YES")
      else:
          print("NO")
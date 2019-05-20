count = int(input())
values = list(map(int,input().split()))

stack = []
output = []
flag = 0

for i in range(len(values)):
    if flag==1:
        flag = 0
        stack.append(values[i])
        pass
    elif values[i]==2 and flag==0:
        if len(stack)==0:
            output.append(-1)
            pass
        else:
            output.append(stack[-1])
            stack.pop()
            pass
    elif values[i]==1 and flag==0:
        flag = 1
        
print(*output)
from functools import reduce

count = int(input())
remaining = list(map(int,input().split()))
remaining_mul = reduce(lambda x, y: x*y, remaining)

mul_left = remaining[0]
remaining.pop(0)
mul_right = int(remaining_mul//mul_left)
output = remaining_mul

for i in range(count-1):
    if mul_left==mul_right:
        output = i
        break
    else:
        if mul_left-mul_right<output:
            output = mul_left-mul_right
        mul_left *= remaining[0]
        mul_right = int(mul_right//remaining[0])
        remaining.pop(0)
        
print(output+1)

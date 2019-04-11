t = int(input())

for x in range(t):
    count = int(input())
    value = list(map(int, input().split()))
    
    if abs(value[-1]-value[0])>26:
        print(-1)
    elif value!=sorted(value):
        print(-1)
    else:
        temp = value[0]
        character = ord('a')
        output = ''
        for i in value:
            if temp==i:
                output+=chr(character)
            else:
                output+=chr(character+abs(temp-i))
        print(output)
            
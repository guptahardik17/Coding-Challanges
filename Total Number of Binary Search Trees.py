# from math import factorial
import sys


_FAC_TABLE = [1, 1]
def factorial(n):
    if n < len(_FAC_TABLE):
        return _FAC_TABLE[n]

    last = len(_FAC_TABLE) - 1
    total = _FAC_TABLE[last]
    for i in range(last + 1, n + 1):
        total *= i
        _FAC_TABLE.append(total)

    return total
    

t = int(sys.stdin.readline())
for i in range(t):
    value = int(sys.stdin.readline())
    if value<2:
        print(1)
        pass
    else:
        print(factorial(value*2)//(factorial(value) * factorial(value+1)))
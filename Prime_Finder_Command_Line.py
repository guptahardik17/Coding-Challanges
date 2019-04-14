import sys

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    
    return True

print(sys.argv)
if len(sys.argv)==1:
    print("first number is missing")
    exit()
elif sys.argv[1].isdigit()==False:
    print("first argument should be a number")
    exit()
elif len(sys.argv)==2:
    print("second number is missing")
    exit()
elif sys.argv[2].isdigit()==False:
    print("second argument should be a number")
    exit()
elif sys.argv[1]>sys.argv[2]:
    print("first number should be less than equal to second number")
    exit()
    
s = int(sys.argv[1])
e = int(sys.argv[2])
l = []

for i in range(s,e+1):
    o = is_prime(i)
    if o==True:
        l.append(i)

if len(l)==0:
    print("not found")
else:
    print(*l)   

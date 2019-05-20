import sys

for x in range(int(sys.stdin.readline())):
    counts_NoUse = sys.stdin.readline()
    
    a = set(list(map(int,sys.stdin.readline().split())))
    b = set(list(map(int,sys.stdin.readline().split())))
    
    option = int(sys.stdin.readline())
    if option==1:
        sys.stdout.write("{"+str(sorted(a.intersection(b)))[1:-1]+"}\n")
        pass
    elif option==2:
        sys.stdout.write("{"+str(sorted(a.union(b)))[1:-1]+"}\n")
        pass
    elif option==3:
        sys.stdout.write("{"+str(sorted(a.symmetric_difference(b)))[1:-1]+"}\n")
        pass
    elif option==4:
        sys.stdout.write("{"+str(sorted(list(a-b)))[1:-1]+"}\n")
        pass
    elif option==5:
        sys.stdout.write("{"+str(sorted(list(b-a)))[1:-1]+"}\n")
        pass
t = int(input())

for i in range(t):
    Knight = list(input().split())
    Jack = list(input().split())
    
    Jacknew = set(Jack) - set(Knight)
    Knightnew = set(Knight) - set(Jack)
    
    
    # print("#"*20,Jacknew,Knightnew)
    if len(Jacknew)==0 and len(Knightnew)>0:
        print("Knight Wins")
    elif len(Knightnew)==0 and len(Jacknew)>0:
        print("Jack Wins")
    elif len(Jacknew)>=0 and len(Knightnew)>=0:
        print("Drawn")
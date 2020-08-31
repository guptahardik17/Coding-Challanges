c = int(input())
colors = input()
numbers = input()
R = []
G = []
B = []

for i in range(c):
    if colors[i] == 'R':
        R.append(int(numbers[i]));
    elif colors[i] == 'G':
        G.append(int(numbers[i]));
    elif colors[i] == 'B':
        B.append(int(numbers[i]));
    
R = sorted(R, reverse=True)
G = sorted(G, reverse=True)
B = sorted(B, reverse=True)

print(R,G,B)

rCounter = 0
gCounter = 0
bCounter = 0
finalNumbers = ''

for i in range(c):
    if colors[i] == 'R':
        finalNumbers += str(R[rCounter])
        rCounter += 1
    elif colors[i] == 'G':
        finalNumbers += str(G[gCounter])
        gCounter += 1
    elif colors[i] == 'B':
        finalNumbers += str(B[bCounter])
        bCounter += 1
        
print(finalNumbers)

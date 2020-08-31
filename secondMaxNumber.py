import ast

def getSecondMax(inp):
    if len(inp) < 2:
        return -1

    maxN, sMaxN = max(inp), min(inp)
    
    if maxN == sMaxN:
        return -1
        
    for index in range(1, len(inp)):
        if inp[index] > maxN:
            sMaxN, maxN = maxN, inp[index]
        elif maxN > inp[index] > sMaxN:
            sMaxN = inp[index]
    
    return sMaxN

if __name__ == "__main__":
    inp = list(map(int, ast.literal_eval(input())))
    print(getSecondMax(inp))
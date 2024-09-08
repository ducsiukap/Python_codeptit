def check(n:str):
    for i in n:
        if (int(i) & 1) == 1: return False
    return True 
    
L = []
def init_():
    for i in range(2, 889, 2):
        s = str(i)
        if (check(s)): L.append(int(s + s[::-1]))

init_()
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in L:
        if i >= n:
            break
        print(i, end=' ')
    print()
def initPrime():
    P = [1] * 501
    P[0] = P[1] = 0
    for i in range(2, 24):
        if (P[i] == 1):
            for j in range(i * i, 501, i):
                P[j] = 0
    return P

def check(n:str, P)->bool:
    if (P[len(n)] == 0): 
        return False

    countPrime = 0
    for char in n:
        countPrime += P[int(char)]
    return countPrime > (len(n) // 2)

t = int(input())
Prime = initPrime()
while t > 0:
    t -= 1
    n = input()
    print("YES" if check(n, Prime) else "NO")
    
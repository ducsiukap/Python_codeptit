import math
def initPrime(n:int)->list:
    P = [1] * (n + 1)
    P[0] = P[1] = 0
    for i in range(2, math.isqrt(n) + 1):
        if (P[i] == 1):
            for j in range(i * i, n + 1, i):
                P[j] = 0
    return P

P=  initPrime(501)
def check(n:str)->bool:
    totalCount, countP = 0, 0
    for i in n:
        if (P[int(i)] == 1):
            countP += 1
        totalCount += 1
    return (P[totalCount] == 1) and (countP > (totalCount >> 1))

t = int(input())
for _ in range(t):
    n = input()
    print("YES" if check(n) else "NO")
    
import math
def initPrime(n:int)->list:
    P = [1] * (n + 1)
    P[0] = P[1] = 0
    for i in range(2, math.isqrt(n) + 1):
        if (P[i] == 1):
            for j in range(i * i, n + 1, i):
                P[j] = 0
    return P

p = initPrime(1000)
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        print(p[a[i][j]], end=' ')
    print()


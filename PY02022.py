import math
def initPrime(n:int)->list:
    P = [1] * (n + 1)
    P[0] = P[1] = 0
    for i in range(2, math.isqrt(n) + 1):
        if (P[i] == 1):
            for j in range(i * i, n + 1, i):
                P[j] = 0
    return P

P = initPrime(1000000)
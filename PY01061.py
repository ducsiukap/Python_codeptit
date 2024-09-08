import math
def initPrime(n:int)->list:
    P = [1] * (n + 1)
    P[0] = P[1] = 0
    for i in range(2, math.isqrt(n) + 1):
        if (P[i] == 1):
            for j in range(i * i, n + 1, i):
                P[j] = 0
    return P

P = initPrime(1000)
t = int(input())
for _ in range(t):
    n = input()
    a = 100 * int(n[0]) + 10 * int(n[1]) + int(n[2])
    b = 100 * int(n[-3]) + 10 * int(n[-2]) + int(n[-1])
    print("YES" if P[a] == 1 and P[b] == 1 else "NO")
    
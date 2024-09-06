def initPrime():
    P = [1] * 10000
    P[0] = P[1] = 0
    for i in range(2, 100):
        if (P[i] == 1): 
            for j in range(i * i, 10000, i):
                P[j] = 0
    return P

t = int(input())
P = initPrime()
while t > 0:
    t -= 1
    n = input()
    n = 1000 * int(n[-4]) + 100 * int(n[-3]) + 10 * int(n[-2]) + int(n[-1])
    print("YES" if P[n] else "NO")
    
def initPrime():
    P = [1] * 4501
    P[1] = P[0] = 0
    for i in range(2, 69):
        if (P[i] == 1):
            for j in range(i * i, 4501, i):
                P[j] = 0
    return P

t = int(input())
Prime = initPrime()
while t > 0:
    t -= 1
    n = input()
    totalSum = 0
    for char in n:
        totalSum += int(char)
    print("YES" if Prime[totalSum] else "NO")
    
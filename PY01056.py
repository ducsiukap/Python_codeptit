def initPrime():
    P = [1] * 4501
    P[0] = P[1] = 1
    for i in range(2, 69):
        if P[i] == 1:
            for j in range(i * i, 4501, i):
                P[j] = 0
    return P

def oddEvenPrime(n:str, Prime)->bool:
    totalSum = 0
    for i in range(len(n)):
        if (i & 1) != (int(n[i]) & 1):
            return False
        totalSum += int(n[i])
    return Prime[totalSum]

Prime = initPrime()
t = int(input())
while t > 0:
    t -= 1
    n = input()
    print("YES" if oddEvenPrime(n, Prime) else "NO")
    
def initPrime()->list:
    P = [1] * 10001
    P[0] = P[1] = 0
    for i in range(2, 101):
        if (P[i] == 1):
            for j in range(i * i, 10001, i):
                P[j] = 0
    prime = []
    for i in range(2, 10001):
        if P[i]: prime.append(i)
    return prime

p = initPrime()
a, b = map(int, input().split())
print(b, end=' ')
for i in range(a):
    b += p[i]
    print(b, end=' ')
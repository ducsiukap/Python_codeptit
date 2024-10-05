t = int(input())
for _ in range(t):
    n = int(input())>>1
    L = list(map(int, input().split()))
    d = {}
    maxf = 0
    x = 10**6 + 1
    for i in L:
        d[i] = d.get(i, 0) + 1
        if d[i] > maxf:
            maxf = d[i]
            x = i
        elif d[i] == maxf: x = min(i, x)
    print(x if maxf > n else 'NO')

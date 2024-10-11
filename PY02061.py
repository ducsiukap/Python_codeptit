t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    h = []
    for i in range(3):
        h.append(list(map(int, input().split())))
    total = 0
    for i in range(n - 2):
        for j in range(m - 2):
            for u in range(3):
                for v in range(3):
                    total += x[i + u][j + v] * h[u][v]
    print(total)

t = int(input())
for _ in range(t):
    n = int(input())
    rd = [0] * 1001
    f, ans = 0, -1
    for _ in range(n):
        x = int(input())
        rd[x] += 1
        if (rd[x] == f):
            ans = min(x, ans)
        if (rd[x] > f):
            ans = x
            f = rd[x]
    print(ans)
    
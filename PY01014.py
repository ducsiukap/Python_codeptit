a, k, n = map(int, input().split())
n -= a

ST = k - (a % k)

if (ST > n): print(-1)
else:
    while ST <= n:
        print(ST, end=' ')
        ST += k

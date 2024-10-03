n = int(input())
b = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans += (b[j] < b[i])
print(ans)

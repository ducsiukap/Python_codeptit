n = int(input())
b = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    ans += abs(b[i] - b[i + 1])
print(ans)

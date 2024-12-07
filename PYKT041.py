import math

n = int(input())

row = []
col = [0 for _ in range(n)]

for i in range(n):
    s = input()
    cnt = 0
    for j in range(n):
        if s[j] == 'C':
            cnt += 1
            col[j] += 1
    row.append(cnt)

ans = 0
for i in range(n):
    ans += row[i] * (row[i] - 1) // 2
    ans += col[i] * (col[i] - 1) // 2

print(ans)
'''
comb(n, 2) = n * (n - 1) // 2

'''
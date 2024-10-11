n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
difference = 0
for i in range(n):
    for j in range(n - i - 1):
        difference += a[i][j] - a[i + j + 1][n - i - 1]
difference = abs(difference)
print('YES' if difference <= k else 'NO', difference, sep='\n')

#   0 1 2 3 4
# 0 0 0 0 0 0
# 1 0 0 0 0 0
# 2 0 0 0 0 0
# 3 0 0 0 0 0
# 4 0 0 0 0 0
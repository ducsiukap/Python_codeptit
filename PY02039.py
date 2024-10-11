n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
difference = 0
for i in range(n):
    for j in range(i + 1, n):
        difference += a[i][j] - a[j][i]
difference = abs(difference)
print('YES' if difference <= k else 'NO', difference, sep='\n')

n = int(input())
a = list(map(float, input().split()))
a.sort()
totalScore = 0.0
k = 0

for i in range(1, n - 1):
    if (a[i] == a[0]) or (a[i] == a[-1]): continue
    totalScore += a[i]
    k += 1

print(f'{(totalScore/k):.2f}')

import math

for _ in range(int(input())):
    a = []
    while len(a) < 2:
        for num in input().split():
            a.append(int(num))

    n, k = a[0], a[1]
    a = a[2:]
    while len(a) < n:
        for num in input().split():
            a.append(int(num))
            
    minLength = n + 1

    for i in range(n):
        if a[i] == k: 
            minLength = 1
            break
        GCD = a[i]
        for j in range(i + 1, n):
            GCD = math.gcd(GCD, a[j])
            if (GCD == k):
                minLength = min(minLength, j - i + 1)
                break
            if GCD < k: 
                break

    print(minLength if minLength <= n else -1)

    
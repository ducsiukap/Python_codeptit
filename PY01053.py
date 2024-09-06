t = int(input())
while t > 0:
    t -= 1
    n = input()
    totalSum = 0
    for char in n:
        totalSum += int(char)
    print("NO" if (totalSum % 3) else "YES")
    
def checkStr(s):
    i, j = 0, len(s) - 1
    while (i < j):
        if (s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

def check(n):
    totalSum = 0
    for char in n:
        totalSum += int(char)
    if (totalSum < 11): return False
    return checkStr(str(totalSum))

t = int(input())
while t:
    t -= 1
    n = input()
    print("YES" if check(n) else "NO")
    
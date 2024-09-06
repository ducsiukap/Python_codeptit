def check(s:str, n)->int:
    a, b, c = 0, 0, 0
    for char in s:
        if char == 'A': a += 1
        elif char == 'B': b += 1
        else: c += 1
    if (a > (n//3)) or (a + b > (2 * n // 3)): return -1
    return (a and b and c and (a <= b) and (b <= c))


n = 4 # int(input())
abc = 'ABC'
ABC = [[] for _ in range(n + 1)]

def initABC(s:str, n):
    for char in abc:
        s += char
        checkResult = check(s, n)
        if checkResult == 1:
            ABC[len(s)].append(s)
        if (checkResult >= 0) and (len(s) < n):
            initABC(s, n)
        s = s[:len(s) - 1]

initABC('', n)
for i in range(3, n+1):
    for item in ABC[i]:
        print(item)
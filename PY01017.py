tTest = int(input())
while tTest:
    tTest -= 1
    s = input()
    
    f = 1
    n:int = len(s)
    for i in range(0, n):
        if (i == n - 1) or (s[i] != s[i + 1]):
            print(f, s[i], sep='', end='')
            f = 1
        else: f += 1
    print()

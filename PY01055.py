def check(n):
    if (len(n) == 1): return True
    if (n[0] == n[1]) or ((len(n) & 1) == 0): return False
    for i in range(2, len(n), 2):
        if (n[i] != n[0]): return False
    return True

t = int(input())
while t > 0:
    t -= 1
    n = input()
    print("YES" if check(n) else "NO")
    
def balanceString(s:str)->bool:
    i, j = 1, len(s) - 2
    while i <= j:
        l = abs(ord(s[i]) - ord(s[i - 1]))
        r = abs(ord(s[j]) - ord(s[j + 1]))
        if (l != r): return False
        i += 1
        j -= 1
    return True

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if balanceString(s) else "NO")
    
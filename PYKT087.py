mod = int(1e9 + 7)

def powMod(n, e):
    if e == 0: return 1
    pwr = powMod(n, e//2)
    if e&1:
        return (((pwr**2) % mod) * n) % mod
    return ((pwr**2)%mod)

for _ in range(int(input())):
    n, k = map(int, input().split())
    np = []
    idx = 0

    while k:
        if k&1: np.append(idx)
        idx += 1
        k //= 2
    
    x = powMod(n, np[0])
    ans = x
    d = {np[0]:x}
    for i in range(1, len(np)):
        exp = np[i] - np[i - 1]
        if d.get(exp) == None:
            d[exp] = powMod(n, exp)
        x *= d[exp] 
        x %= mod
        ans += x
        ans %= mod
    
    print(ans)

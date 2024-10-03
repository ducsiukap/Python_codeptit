def fitList(a:list, b:list, n:int)->bool:
    a.sort()
    b.sort()
    for i in range(n):
        if (a[i] > b[i]):
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES" if fitList(a, b, n) else "NO")

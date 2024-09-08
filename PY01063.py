def countN(s:str, n:str)->int:
    cnt = 0
    while True:
        i:int = s.find(n)
        if (i == -1): break
        cnt += 1
        s = s[i + len(n):]
    return cnt

t = int(input())
for _ in range(t):
    s = input()
    n = input()
    print(countN(s, n))
    
L = list(map(int, input().split()))
while L != [0, 0, 0, 0]:
    cnt = 0
    while L.count(L[0]) != 4:
        cnt += 1
        x = L[0]
        L[0] = abs(L[0] - L[1])
        L[1] = abs(L[1] - L[2])
        L[2] = abs(L[2] - L[3])
        L[3] = abs(L[3] - x)
    print(cnt)
    L = list(map(int, input().split()))

P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

if __name__ == '__main__':
    dictP = {}
    k:int = 0
    for i in P:
        dictP[i] = k
        k += 1

    while True:
        L = input().split()
        if len(L) == 1: break
        n, s = L
        k = int(n)
        for i in reversed(range(0, len(s))):
            j = dictP.get(s[i])
            print(P[(j + k) % 28], end='')
        print()

def intRev(n: int):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n //= 10
    return res

def initErimpNumberArray():
    P = [1] * 1000001
    P[0] = P[1] = 1
    for i in range(2, 1001):
        if P[i] == 1:
            for j in range(i * i, 1000001, i):
                P[j] = 0
    EN = [0] * 1000001
    for i in range(13, 1000001):
        if P[i] == 1:
            REV = intRev(i)
            if (REV <= i) or (P[REV] == 0):
                EN[i] = 0
            else: EN[i] = REV
    return EN

if __name__ == '__main__':
    ENarr = initErimpNumberArray()
    T = int(input())
    while T:
        T -= 1
        n = int(input())
        for i in range(13, n):
            if (ENarr[i] != 0) and (ENarr[i] < n):
                print(i, ENarr[i], end=' ')
        print()


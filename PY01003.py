def intRound(L):
    inc = 0
    lenL = len(L)
    for i in range(1, lenL):
        if L[i] == '4':
            continue
        else:
            inc = (L[i] > '4')
            break
    res = int(L[0]) + inc
    res *= (10 ** (lenL - 1))
    return res

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        T -= 1
        n = input()
        print(intRound(n))

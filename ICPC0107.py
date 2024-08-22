def _sum(x1): # int[] array -> int number
    # [1, 2] -> 12
    res = 0
    for i in range(0, len(x1)):
        res = res * 10 + x1[i]
    return res

def calc(x1, x2, p, q):
    n1, n2 = len(x1), len(x2)
    X1 = []
    X2 = []
    for i in range(0, n1):
        if x1[i] == p:
            X1.append(int(q))
        else: X1.append(int(x1[i]))
    for i in range(0, n2):
        if x2[i] == p:
            X2.append(int(q))
        else: X2.append(int(x2[i]))
    return _sum(X1) + _sum(X2)

# main function
if __name__ == '__main__':
    T = int(input())
    while T:
        T -= 1
        p, q = input().split()
        s = input().split()
        if len(s) > 1:
            a, b = s[0], s[1]
        else:
            a = s[0]
            b = input()
        maxpq = max(p, q)
        minpq = min(p, q)
        print(calc(a, b, maxpq, minpq), calc(a, b, minpq, maxpq))

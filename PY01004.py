import math
P = [1] * 10001

def check(n)->str:
    if n <= 2:
        return "NO"
    k = 2
    for i in range(2, n - 1):
        if math.gcd(i, n) == 1:
            k += 1
    return "YES" if P[k] == 1 else "NO"

if __name__ == '__main__':
    for i in range (2, 101):
        if P[i] == 1:
            for j in range(i * i, 10001, i):
                P[j] = 0
    T = int(input())
    while T > 0:
        T -= 1
        n = int(input())
        print(check(n))

def isPrime(n)->bool:
    i = 2
    while i * i <= n:
        if (n % i) == 0:
            return False
        i += 1
    return True

def checkRev(n)->bool:
    res = 0
    while n > 0:
        x = n % 10
        if (x != 2) and (x != 3) and (x != 5) and (x != 7):
            return False
        res = res * 10 + x
        n //= 10
    return isPrime(res)

if __name__ == '__main__':
    T = int(input())
    while T:
        T -= 1
        n = int(input())
        if isPrime(n) and checkRev(n): print("Yes")
        else: print("No")

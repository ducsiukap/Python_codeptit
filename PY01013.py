import math

def check(n: int)->bool:
    totalSum = 0
    while n:
        totalSum += (n % 10)
        n //= 10
    i:int = 2
    while i * i <= totalSum:
        if totalSum % i == 0:
            return False
        i += 1
    return (totalSum > 1)


if __name__ == '__main__':
    tTest = int(input())
    for test in range(0, tTest):
        a, b = map(int, input().split())
        print("YES" if check(math.gcd(a, b)) else "NO")

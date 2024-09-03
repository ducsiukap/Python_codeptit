import math

if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        a = input()
        b = int(a[::-1])
        a = int(a)
        print("YES" if math.gcd(a, b) == 1 else "NO")
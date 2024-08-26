import math

if __name__ == '__main__':
    T = int(input())
    while T:
        T -= 1
        a, r, m = map(float, input().split())
        n = math.ceil(math.log(m / a) / math.log(1 + r / 100))
        print(n)
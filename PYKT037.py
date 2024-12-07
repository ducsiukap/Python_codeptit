s = '0123456789ABCDEFGHIJKLMNOPQRSTUVwXYZ'

for _ in range(int(input())):
    n, b = map(int, input().split())
    res = ''
    while n > 0:
        res = s[n % b] + res
        n //= b
    print(res)
    
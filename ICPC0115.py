gt = [1] * 10
def checkKrish(n)->str:
    tmp = n
    res = 0
    while tmp > 0:
        res += gt[tmp % 10]
        tmp //= 10

    return "Yes" if res == n else "No"


if __name__ == '__main__':
    for i in range(2, 10):
        gt[i] = gt[i - 1] * i
    T = int(input())
    while T > 0:
        T -= 1
        n = int(input())
        print(checkKrish(n))

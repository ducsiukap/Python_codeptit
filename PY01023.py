
if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        n = int(input())
        if (n == 1): print(1)
        else:
            print("1 * ", end='')
            i = 2
            while (i <= n):
                cnt = 0
                while n % i == 0:
                    n /= i
                    cnt += 1
                if (cnt > 0): 
                    print(f'{i}^{cnt}', end=' ')
                    if (n != 1): print('*', end=' ')
                i += 1
            print()
            
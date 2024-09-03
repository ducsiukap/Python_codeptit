
if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        n = int(input())
        ans:float = 0
        while n > 0:
            ans += 1/n
            n -= 2
        print(f'{ans:.6f}')
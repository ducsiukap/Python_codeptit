def hanoiTower(n:int, src, dst, tmp):
    if n == 1: print(f'{src}->{dst}')
    else:
        hanoiTower(n-1, src, tmp, dst)
        print(f'{src}->{dst}')
        hanoiTower(n - 1, tmp, dst, src)

if __name__ == '__main__':
    # tTest = int(input())
    tTest = 1
    while tTest > 0:
        tTest -= 1
        n = int(input())
        hanoiTower(n, 'A', 'C', 'B')

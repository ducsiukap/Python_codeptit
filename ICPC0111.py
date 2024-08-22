if __name__ == '__main__':
    T = int(input())
    while (T):
        T -= 1
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        for i in range(0, n):
            print(arr[(i + k) % n], end=' ')
        print()



#main func
if __name__ == '__main__':
    T = int(input())
    while T:
        T -= 1
        n = int(input())
        arr = list(map(int, input().split()))

        _1stmin = arr[0]
        _2ndmin = arr[0]
        _3rdmin = arr[0]

        for i in range(1, n):
            if arr[i] <= _1stmin:
                _3rdmin = _2ndmin
                _2ndmin = _1stmin
                _1stmin = arr[i]
            elif arr[i] <= _2ndmin:
                _3rdmin = _2ndmin
                _2ndmin = arr[i]
            elif arr[i] < _3rdmin:
                _3rdmin = arr[i]
        print(_1stmin + _2ndmin + _3rdmin)

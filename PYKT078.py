for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(num) for num in input().split()]

    iMax = 0
    for i in range(1, n):
        if a[i] > a[iMax]:
            iMax = i
    a.insert(iMax, m)
    positive = []
    negative = []
    for num in a:
        if num < 0: 
            negative.append(num)
        else:
            positive.append(num)
    a = negative + positive
    for num in a:
        print(num, end=' ')
    print()
    
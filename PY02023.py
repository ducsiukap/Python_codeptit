t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mark = [[] for _ in range(100)]
    for num in a:
        mark[sum([int(i) for i in str(num)])].append(num)
    for item in mark:
        if (len(item) == 0): continue
        item.sort()
        for num in item:
            print(num, end=' ')
    print()
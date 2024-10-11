t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mark = {}
    for num in a:
        mul = 1
        for i in str(num):
            mul *= int(i)
        if mark.get(mul) == None: mark[mul] = [num]
        else: mark[mul].append(num)
    keys = sorted(mark.keys())
    for key in keys:
        mark[key].sort()
        for num in mark[key]:
            print(num, end=' ')
    print()

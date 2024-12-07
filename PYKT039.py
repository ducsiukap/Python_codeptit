for _ in range(int(input())):
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]

    a.sort()
    b.sort()

    checkpoint = False
    for i in range(n):
        if a[i] > b[i]:
            checkpoint = True
            break
    print ('NO' if checkpoint else 'YES')
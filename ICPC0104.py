from curses.ascii import isdigit

T = int(input())

while T > 0:
    s = input()

    ans = int(1e18)
    tmp = 0

    for i in s:
        if isdigit(i):
            tmp = tmp * 10 + int(i)
        elif tmp != 0:
            ans = min(ans, tmp)
            tmp = 0

    print(ans)
    T -= 1
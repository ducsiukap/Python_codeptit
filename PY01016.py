tTest = int(input())
while tTest:
    tTest -= 1
    s = input()
    for i in range(1, len(s), 2):
        f = int(s[i])
        print(s[i - 1] * f, end='')
    print()


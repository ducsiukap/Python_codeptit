
T = int(input())

while T > 0:
    s = input()
    num = [0]
    for char in s:
        if char.isdigit():
            num.append(num[-1] * 10 + int(char))
        else:
            num.append(0)
    ans = max(num)
    print(ans)
    T -= 1

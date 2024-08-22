T = int(input())
while T > 0:
    T -= 1
    s = input()
    print("Yes" if s[0] == s[-1] else "No")

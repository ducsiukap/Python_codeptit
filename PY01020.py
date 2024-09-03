
if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        s = input()
        print("YES" if ((s[len(s) - 1] == '6') and (s[len(s) - 2] == '8')) else "NO")
        
if __name__ == '__main__':
    tTest = int(input())
    while tTest:
        tTest -= 1
        n = input()
        print("YES" if ((n[0] == n[-2]) and (n[1] == n[-1])) else "NO")
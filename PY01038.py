
if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        n = input()
        ok = False
        for i in range(0, 1001):
            if (int(n) % 7 == 0):
                ok = True
                break
            else:
                a = int(n[::-1]) + int(n)
                n = str(a)
        print(n if ok else -1)

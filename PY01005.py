def check(n):
    cnt = 0
    for i in range(0, len(n)):
        if (n[i] == '4') or (n[i] == '7'):
            cnt += 1
    return "YES" if (cnt == 4) or (cnt == 7) else "NO"

if __name__ == '__main__':
    n = input()
    print(check(n))

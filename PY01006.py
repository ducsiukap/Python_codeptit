def check(n):
    for i in range(0, len(n)):
        if (n[i] != '4') and (n[i] != '7'):
            return "NO"
    return "YES"

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        T -= 1
        n = input()
        print(check(n))

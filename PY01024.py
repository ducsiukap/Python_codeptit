def check(n:list)->bool:
    totalSum = n[0]
    for i in range(1, len(n)):
        if abs(n[i] - n[i - 1]) != 2:
            return False
        totalSum += n[i]
    return totalSum % 10 == 0

if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        n = input()
        m = [int(i) for i in n]
        print("YES" if check(m) else "NO")
        
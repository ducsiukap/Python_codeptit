def perfectNumber(n:str)->bool:
    if (n[0] == n[1]): return False
    for i in range(2, len(n)):
        if (n[i] != n[i % 2]): return False
    return True

if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        n = input()
        print("YES" if perfectNumber(n) else "NO")

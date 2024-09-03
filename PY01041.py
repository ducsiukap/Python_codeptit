def check(n:str)->bool:
    if (len(n) < 3): return False
    i:int = 1
    while i < len(n):
        if (n[i] == n[i - 1]): return False
        if (n[i] < n[i - 1]): break
        i += 1
    j:int = len(n) - 2
    while j >= 0:
        if (n[j] == n[j + 1]): return False
        if (n[j] < n[j + 1]): break
        j -= 1
    i -= 1
    j += 1
    return (i == j)

if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        n = input()
        print("YES" if check(n) else "NO")
        
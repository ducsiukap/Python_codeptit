def check(s:str)->bool:
    for i in range(1, len(s)):
        if (s[i] < s[i - 1]): return False
    return True

if __name__ == '__main__':
    tTest = int(input())
    while tTest:
        tTest -= 1
        s = input()
        print("YES" if check(s) else "NO")

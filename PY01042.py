def check(n:str)->bool:
    for i in n:
        unc = ord(i)
        if (unc < ord('0')) or (unc > ord('2')): return False
    return True

if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        n = input()
        print("YES" if check(n) else "NO")
        
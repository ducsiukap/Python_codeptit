num = '02468'
ans = []
def check(s:str, n:str)->bool:
    if (s[0] == '0') or (len(s) > len(n)): return False
    return int(s) < int(n)

def nInit(s:str, n:str, i):
    for j in num:
        ss = s[:i-1] + j + j + s[i-1:]
        if check(ss, n):
            ans.append(int(ss))
            nInit(ss, n, i + 1)

if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        ans.clear()
        tTest -= 1
        n = input()
        nInit('', n, 1)
        ans.sort()
        for i in ans: print(i, end=' ')
        print()
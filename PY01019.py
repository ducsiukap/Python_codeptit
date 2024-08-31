
def equalsDistance(s:str)->bool:
    i = 1
    j = len(s) - 1 - i
    while i < j:
        left = abs(ord(s[i]) - ord(s[i - 1]))
        right = abs(ord(s[j]) - ord(s[j + 1]))
        if left != right:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    tTest = int(input())
    # tTest = 1
    while tTest > 0:
        tTest -= 1
        s = input()
        print("YES" if equalsDistance(s) else "NO")

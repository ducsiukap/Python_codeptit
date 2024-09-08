def calc(s:str):
    totalSum = 0
    for i in s[1::2]:
        totalSum += int(i)

    mul = 1
    ok = False
    for i in s[::2]:
        if i != '0':
            mul *= int(i)
            ok = True
    
    print(mul if ok else 0, totalSum)

t = int(input())
while t > 0: 
    t -= 1
    n = input()
    calc(n)
    
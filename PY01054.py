t = int(input())
while t > 0:
    t -= 1
    n = input()
    mul = 1
    for char in n:
        if char == '0':
            continue
        mul *= int(char)
    print(mul)
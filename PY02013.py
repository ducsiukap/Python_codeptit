L = [0] * 100001
for i in range(17):
    L[2 ** i] = i + 1

def calc(n:int):
    if L[n] == 0:
        L[n] = 1 + calc(n*3+1 if n&1 else n>>1)
    return L[n]

n = int(input())
while n != 0:
    print(calc(n))
    n = int(input())
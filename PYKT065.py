import math
p = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 0]

x = [0 for _ in range(17)]
def Try(idx:int, n:int, k:int, where:list):
    for j in range(x[idx - 1] + 1, n - k + idx + 1):
        x[idx] = j
        # print(f'n:{n}, k:{k}, idx:{idx} -> {x[1:idx+1]}')
        if idx == k:
            lcm = 1
            for i in range(1, idx + 1):
                lcm *= p[x[i]]
            where.append(lcm)
        else: 
            Try(idx + 1, n, k, where)

mark = []
for n in range(1, 16):
    inc = []
    dec = []
    for k in range(1, n + 1):
        if k & 1: 
            Try(1, n, k, dec)
        else: 
            Try(1, n, k, inc)
    mark.append((dec, inc))
# print(mark)

i = -1
mp = {}
for n in range(2, 51):
    if n == p[i + 2]:
        i += 1
    mp[n] = i
# print(map)

while True:
    s = input()
    if (s == '-1'): break

    l, r = map(int, s.split())
    n = int(input())
    dec, inc = mark[mp[n]]
    cnt = r - l + 1

    for num in dec:
        st = ((l - 1 + num) // num) * num
        if (st > r): continue
        en = (r // num) * num
        cnt -= (en - st) // num + 1

    for num in inc:
        st = ((l - 1 + num) // num) * num
        if (st > r): continue
        en = (r // num) * num
        cnt += (en - st) // num + 1

    print(cnt)

    '''1 10 10
    cnt = 10
    dec: 
        st = 2, en = 10 => cnt = 5
        st = 3, en = 9 => cnt = 2
        st = 5, en = 10 => cnt = 0
        st = 7, en = 7 => cnt = -1

    inc:
        st = 6, en = 6, cnt = 0
        st = 10, en = 10, cnt = 1

    '''
    
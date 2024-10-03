from collections import deque

def takeHammingSequence():
    L = []
    Max = 10**18 + 1
    q = deque()
    q.append((1, 2))
    while len(q) > 0:
        k, v = q.popleft()
        if (k < Max):
            L.append(k)
            if v == 2:
                q.append((k << 1, 2))
                q.append((k * 3, 3))
                q.append((k * 5, 5))
            elif v == 3:
                q.append((k * 3, 3))
                q.append((k * 5, 5))
            else: 
                q.append((k * 5, 5))
    return L

Hamming = sorted(takeHammingSequence())

def binSearch(num:int):
    l, r = 0, 10916
    while l <= r:
        mid = (l + r) >> 1
        if Hamming[mid] == num: return (mid + 1)
        if Hamming[mid] < num: l = mid + 1
        else: r = mid - 1
    return 'Not in sequence'

t = int(input())
for _ in range(t):
    n = int(input())
    print(binSearch(n))

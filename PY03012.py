from functools import cmp_to_key
def cmp(a:list, b:list):
    if a[1] == b[1]:
        if a[2] == b[2]:
            return -1 if a[0] < b[0] else 1
        return -1 if a[2] < b[2] else 1
    return -1 if a[1] > b[1] else 1

n = int(input())
infors = [[] for _ in range(n)]
for i in range(n):
    infors[i].append(input())
    infors[i].extend(map(int, input().split()))

infors.sort(key=cmp_to_key(cmp))
for infor in infors:
    print(infor[0], infor[1], infor[2])
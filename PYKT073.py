n = int(input())
a = []
for _ in range(n):
    a.append(input().split())

flag = False
i = 0
type = []
while i < n:
    if len(a[i]) != 7:
        if not flag:
            flag = True
            type.append(1)
        i += 2
    else: 
        flag = False
        i += 4
        type.append(2)

n = len(type)
print(n)
for j in range(n):
    print(type[j])


a = []
while len(a) < 10:
    a.extend(list(map(int, input().split())))
mod42 = [0]*42
for num in a:
    mod42[num % 42] = 1
print(sum(mod42))

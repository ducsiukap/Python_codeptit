n = input()
k = len(n) % 3
if k == 0: k += 3
while k < len(n):
    n = f'{n[:k]},{n[k:]}'
    k += 4
print(n)
import itertools

s = input()

# Sinh tất cả các tổ hợp chập K của A
combinations = itertools.permutations(s)
# In kết quả
for combination in combinations:
    for _ in combination:
        print(_, end='')
    print()

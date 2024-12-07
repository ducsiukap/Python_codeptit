np = input()

np = '0' * ((3 - len(np) % 3) % 3) + np

d = {'000' : '0', '001' : '1', '010' : '2', '011' : '3',
     '100' : '4', '101' : '5', '110' : '6', '111' : '7'}

res = ''
for i in range(0, len(np), 3):
    res += d.get(np[i:i+3])
print(res)
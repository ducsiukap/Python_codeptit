Hash = {0:0, 1:1, 10:2, 11:3, 
        100:4, 101:5, 110:6, 111:7, 
        1000:8, 1001:9, 1010:10, 1011:11, 1100:12, 1101:13, 1110:14, 1111:15}

for _ in range(int(input())):
    base = int(input())
    binary = input()
    if base == 2:
        print(binary)
    else:
        base = 2 if base == 4 else 3 if base == 8 else 4
        mod = len(binary) % base
        if mod != 0:
            mod = base - mod
        binary = '0'*mod + binary
        print(binary)
        for i in range(0, len(binary), base):
            print(Hash.get(int(binary[i:i+base]), 0), end='')
        print()

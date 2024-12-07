def getFee(type, slot):
    match type:
        case 't': 
            return 20000
        case 'c':
            return 10000 if slot == '5' else 15000
        case default:
            return 50000 if slot == '29' else 70000

thongke = {}

for _ in range(int(input())):
    info = input().split()
    if info[3][0] == 'O':
        continue
    thongke[info[-1]] = thongke.get(info[-1], 0) + getFee(info[1][3], info[2])

for (day, total) in thongke.items():
    print(f'{day}: {total}')

        
        
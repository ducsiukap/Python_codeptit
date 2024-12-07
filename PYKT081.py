for _ in range(int(input())):
    IP = input().split('.')
    if len(IP) != 4: print("NO")
    else: 
        isValid = True
        for i in range(4):
            try:
                x = int(IP[i])
                if x < 0 or x > 255:
                    isValid = False
                    break
            except:
                isValid = False
                break
        print("YES" if isValid else "NO")
        

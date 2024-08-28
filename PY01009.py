

if __name__ == '__main__':
    s = input()
    lwr:int = 0
    for i in s:
        lwr += (i >= 'a')
    
    print(s.lower() if lwr >= (len(s) - lwr) else s.upper())


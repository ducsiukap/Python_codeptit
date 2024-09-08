t = int(input())
cnt = 0
dictVal = {}
while t > 0: 
    t -= 1
    s = input()
    if dictVal.get(s, False) == False:
        cnt += 1
        dictVal[s] = True
print(cnt)
    
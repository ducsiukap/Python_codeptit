word = []
while True:
    try:
        word.extend(input().split())
    except Exception:
        break
fw = True
for i in range(len(word)):
    w = word[i].lower()
    if fw == True:
        w = w[0].upper() + w[1:]
        fw = False
    if w[-1] in '.!?':
        fw = True
        w = w[:len(w) - 1] + '\n'
    else: w += ' '
    print(w, end='')
    
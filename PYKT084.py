isSubject = True
Subject = None
numOfQuestion = 0

mark = {}
for _ in range(int(input())):
    s = input()
    if isSubject: 
        Subject = s
        isSubject = False
    elif s == '':
        isSubject = True
        mark[Subject] = mark.get(Subject, 0) + numOfQuestion
        numOfQuestion = 0
    else: numOfQuestion += 1

if numOfQuestion != 0:
    mark[Subject] = mark.get(Subject, 0) + numOfQuestion
    
for (sub, q) in mark.items():
    print(f'{sub}: {q}')

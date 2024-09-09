valid = "abcdefghijklmnopqrstuvwxyz._"

def check(s:str):
    for i in s:
        if (i not in valid): 
            return False
    return True

def check2(s:str):
    L = s.split('.')
    return (len(L) > 1) and (L[-1] == 'py')


s = input()
s = s.lower()
print('yes' if check(s) and check2(s) else 'no')

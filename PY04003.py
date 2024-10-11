import math
class PhanSo:
    def __init__(self, t, m):
        x = math.gcd(t, m)
        self.t = t//x
        self.m = m//x
    def __str__(self):
        return f'{self.t}/{self.m}'
    
t, m = map(int, input().split())
p = PhanSo(t, m)
print(p)
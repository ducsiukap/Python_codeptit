import math
class PhanSo:
    def __init__(self, t, m):
        x = math.gcd(t, m)
        self.t = t//x
        self.m = m//x
    def plus(self, other):
        M = self.m * other.m // math.gcd(self.m, other.m)
        T = self.t * M // self.m + other.t * M // other.m
        return PhanSo(T, M)
    def __str__(self):
        return f'{self.t}/{self.m}'

a = input().split()
p1 = PhanSo(int(a[0]), int(a[1]))
p2 = PhanSo(int(a[2]), int(a[3]))
print(p1.plus(p2))
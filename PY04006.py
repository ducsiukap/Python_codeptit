import math


class Point0406:
    def __init__(self, points):
        self.A = (points[0], points[1])
        self.B = (points[2], points[3])
        self.C = (points[4], points[5])
        self.AB = self.__distance(self.A, self.B)
        self.AC = self.__distance(self.A, self.C)
        self.BC = self.__distance(self.B, self.C)

    def __distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def area(self):
        # if (self.AB + self.AC <= self.BC) or (self.AB + self.BC <= self.AC) \
        #         or (self.AC + self.BC <= self.AB):
        #     print('INVALID')
        # elif (abs(self.AB - self.AC) >= self.BC) or (abs(self.AB - self.BC) >= self.AC) \
        #         or (abs(self.AC - self.BC) >= self.AB):
        #     print('INVALID')
        if 2*max(self.AB, self.AC, self.BC) >= self.AB + self.AC + self.BC:
            print('INVALID')
        else:
            a, c, b = self.AB, self.AC, self.BC
            d = math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            print(f'{d:.2f}')

n = int(input())
points = []
for _ in range(n):
    points.extend([float(i) for i in input().split()])

i = 0
while i < n:
    idx = 6*i
    triangle = Point0406(points[idx:idx+6])
    triangle.area()
    i += 1


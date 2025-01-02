import math


class Point0405:
    def __init__(self, points):
        self.A = (points[0], points[1])
        self.B = (points[2], points[3])
        self.C = (points[4], points[5])
        self.AB = self.__distance(self.A, self.B)
        self.AC = self.__distance(self.A, self.C)
        self.BC = self.__distance(self.B, self.C)

    def __distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def perimeter(self):
        # if (self.AB + self.AC <= self.BC) or (self.AB + self.BC <= self.AC) \
        #         or (self.AC + self.BC <= self.AB):
        #     print('INVALID')
        # elif (abs(self.AB - self.AC) >= self.BC) or (abs(self.AB - self.BC) >= self.AC) \
        #         or (abs(self.AC - self.BC) >= self.AB):
        #     print('INVALID')
        if 2*max(self.AB, self.AC, self.BC) >= self.AB + self.AC + self.BC:
            print('INVALID')
        else:
            print(str.format('{0:.3f}', self.AB + self.AC + self.BC))

n = int(input())
points = []
for _ in range(n):
    points.extend([float(i) for i in input().split()])

i = 0
while i < n:
    idx = 6*i
    triangle = Point0405(points[idx:idx+6])
    triangle.perimeter()
    i += 1


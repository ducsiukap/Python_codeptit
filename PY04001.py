from decimal import Decimal
import math
class Point:
    def __init__(this, a, b):
        this.x = a
        this.y = b
    def distance(this, other):
        X = this.x - other.x
        Y = this.y - other.y
        return f'{math.sqrt(X*X + Y*Y):.4f}'

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1

        
class TimeUsed:
    def __init__(self, id, name, timeIn, timeOut):
        self.id = id
        self.name = name
        self.hh, self.mm = self.__calcTime(timeIn, timeOut)

    def __lt__(self, other):
        return (self.hh, self.mm) > (other.hh, other.mm)

    def __calcTime(self, timeIn, timeOut):
        times = [int(i) for i in timeIn.split(':')] + [int(i) for i in timeOut.split(':')]
        totalTime = (times[2] - times[0])*60 + (times[3] - times[1])
        return totalTime//60, totalTime%60

    def __str__(self):
        return f'{self.id} {self.name} {self.hh} gio {self.mm} phut'

n = int(input())
users = []
for _ in range(n):
    users.append(TimeUsed(input(), input(), input(), input()))
for u in sorted(users):
    print(u)


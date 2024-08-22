def DecimalToNBase(Dec, N):
    Hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    Nbase = []
    while Dec:
        Nbase.append(Hexa[Dec % N])
        Dec //= N
    for i in range(-1, -1 - len(Nbase), -1):
        print(Nbase[i], end='')
    print() # endl

# main function
if __name__ == '__main__':
    T = int(input())

    while T > 0:
        T -= 1
        b = int(input())
        BinaryString = input()

        if b == 2:
            print(BinaryString)
            continue

        Dec = 0
        n = len(BinaryString)

        for i in range(0, n):
            Dec += int(BinaryString[n - i - 1]) * (2 ** i)

        DecimalToNBase(Dec, b)
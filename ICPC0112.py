def countPrimeDivisorArray()->list:
    P = [1] * 1000001
    P[0] = P[1] = 0
    for i in range(2, 1001):
        if P[i] == 1:
            for j in range(i * i, 1000001, i):
                P[j] = 0
    pd = [0] * 1000001
    for i in range(11, 1000001):
        pd[i] = pd[i - 1]
        pd[i] += P[i] * P[i - 6] * (P[i - 2] + P[i - 4])
    return pd

if __name__ == "__main__":
    cpd = countPrimeDivisorArray()

    T = int(input())
    while T:
        T -= 1
        n = int(input())
        print(cpd[n])
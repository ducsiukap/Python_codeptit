n, m = map(int, input().split())
matrix = []
covidPosition = []

for i in range(n):
    row = input().split()
    for j in range(m):
        x = int(row[j])
        matrix.append(x)
        if (x == -1):
            covidPosition.append((i, j))

def insideMatrix(r, c):
    if (r < 0) or (r >= n) or (c < 0) or (c >= m): 
        return -1
    return r*n + c

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
checked = [False for _ in range(n * m)]
unsafe = 0
for (r, c) in covidPosition:
    for i in range(8):
        idx = insideMatrix(r + dy[i], c + dx[i])
        if (idx != -1) and (checked[idx] == False):
            unsafe += matrix[idx]
            checked[idx] = True

print(unsafe)


n = int(input())
inputList = list(map(int, input().split()))

arr = [inputList[0]]
topArr = 0

for i in range(1, n):
    if (topArr != -1) and ((inputList[i] + arr[topArr]) & 1 == 0):
        del arr[topArr]
        topArr -= 1
    else:
        arr.append(inputList[i])
        topArr += 1

print(topArr + 1)

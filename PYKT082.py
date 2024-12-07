point = [1, 1, 1, 2.5, 2.5, 3.0, 3.0, 3.5, 3.5, 3.5, 4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 5, 5.5, 5.5, 5.5, 
         6, 6, 6, 6, 6.5, 6.5, 6.5, 7, 7, 7, 7.5, 7.5, 8, 8, 8.5, 8.5, 9, 9]
for _ in range(int(input())):
    result = [float(x) for x in input().split()]
    result[0] = point[int(result[0])]
    result[1] = point[int(result[1])]

    overall = sum(result) / 4
    x = overall % 1
    overall = int(overall) + float(0 if x < 0.25 else 0.5 if x < 0.75 else 1)
    print(overall)


import re # regex
import heapq 

t = int(input())
for z in range(t):
    input()
    inp = ' ' + input().replace(' ', '  ') + ' '
    # so trong chuoi se co dang ' num ', muc dich la cô lập cac so
    pq = []
    n = -8
    # n < 0 -> so nguyen am co n chu so
    # n > 0 -> so nguyen duong co n chu so
    # -1e8 <= a[i] < 1e8 => -8 <= n <= 8
    while n <= 8 and len(pq) <= 3:
        # neu len(pq) > 3 -> da tim duoc 3 phan tu nho nhat, ko tim nua
        if (n == 0): 
            n += 1
            continue
        regex = '\\d' * abs(n) + ' ' # regex
        if n < 0 :
            regex = '-' + regex
        elif n > 0 :
            regex = ' ' + regex
        
        n += 1
        
        # find all number which matches regex
        for num in re.findall(regex, inp):
            pq.append(int(num))
    
    # print(pq)
    pq.sort()
    print(sum(pq[:3]))


for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    L, R = a[0], a[0]
    st = {a[0]}

    for i in range(1, n):
        L = min(a[i], L)
        R = max(a[i], R)
        st.add(a[i])
    
    print(R - L + 1 - len(st))


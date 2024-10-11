t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    st = []
    ans = []
    for i in range(n):
        while (len(st) > 0) and (a[st[-1]] <= a[i]):
            st.pop()
        ans.append(i + 1 if len(st) == 0 else i - st[-1])
        st.append(i)
    for answ in ans:
        print(answ, end=' ')
    print()
    
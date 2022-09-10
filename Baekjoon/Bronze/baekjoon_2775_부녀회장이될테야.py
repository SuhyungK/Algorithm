def f():
    for i in range(1, n+1):
        for j in range(k):
            lst[i][j] = sum(lst[i-1][:j+1])

T = int(input())
for _ in range(T):
    n = int(input())
    k = int(input())
    lst = [[0] * k for _ in range(n+1)]
    for i in range(k):
        lst[0][i] = i+1

    f()
    print(lst[n][k-1])
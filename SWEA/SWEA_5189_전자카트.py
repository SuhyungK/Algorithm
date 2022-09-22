def f(i, k, lst):
    global minV
    if i == k:
        s = sum([arr[lst[l-1]][lst[l]] for l in range(N)])
        if minV > s:
            minV = s

    for j in range(N):
        if j not in lst:
            f(i+1, k, [j]+lst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 1e9

    f(1, N, [0])
    print(f'#{tc}', minV)
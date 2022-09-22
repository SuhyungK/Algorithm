def dfs(s, d):
    global minV
    if s == N:
        if minV > d:
            minV = d
            return

    if minV < d:
        return

    for v, w in arr[s]:
        dfs(v, d+w)

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    minV = 1e9

    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s] += [(e, w)]

    dfs(0, 0)
    print(f'#{tc}', minV)
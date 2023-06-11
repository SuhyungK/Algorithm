# 최소합

def dfs(si, sj, s):
    global res
    if (si, sj) == (N - 1, N - 1):
        if res > s:
            res = s

    if res < s:
        return

    if 0 <= si < N and 0 <= sj < N-1:
        dfs(si, sj+1, s+arr[si][sj+1])
    if 0 <= si < N-1 and 0 <= sj < N:
        dfs(si+1, sj, s+arr[si+1][sj])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = N ** N

    dfs(0, 0, arr[0][0])
    print(f'#{tc}', res)
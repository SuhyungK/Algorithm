# 최소 비용

from collections import deque

T = int(input())
res = [0] * T

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[1e9] * N for _ in range(N)]
    q = deque()

    q.append((0, 0))
    v[0][0] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if -1 < nr < N and -1 < nc < N:
                fuel = 0 if arr[nr][nc] <= arr[r][c] else arr[nr][nc] - arr[r][c]
                if v[nr][nc] > v[r][c] + fuel + 1:
                    v[nr][nc] = v[r][c] + fuel + 1
                    q.append((nr, nc))

    res[tc - 1] = v[N - 1][N - 1]

for tc in range(1, T + 1):
    print(f'#{tc}', res[tc - 1])
# 알고스팟

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[1e9] * M for _ in range(N)]

q = [(0, 0)]
v[0][0] = 0
while q:
    r, c = q.pop(0)
    for dr, dc in (-1, 0), (1, 0), (0, 1), (0, -1):
        nr, nc = r + dr, c + dc
        if -1 < nr < N and -1 < nc < M and v[nr][nc] > v[r][c] + arr[nr][nc]:
            v[nr][nc] = v[r][c] + arr[nr][nc]
            q.append((nr, nc))

print(v[N - 1][M - 1])

# 도넛 행성
from collections import deque

N, M = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(N)]

def find_forest(r, c):
    q = deque()
    planet[r][c] = 1
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
            nr = _r % N if (_r:=r + dr) >= 0 else _r + N
            nc = _c % M if (_c:=c + dc) >= 0 else _c + M
            if -1 < nr < N and -1 < nc < M and planet[nr][nc] == 0:
                planet[nr][nc] = 1
                q.append((nr, nc))

total_cnt = 0
for i in range(N):
    for j in range(M):
        if planet[i][j] == 0:
            find_forest(i, j)
            total_cnt += 1

print(total_cnt)


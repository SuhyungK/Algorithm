# 내리막 길

from heapq import heappop, heappush

m, n = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(m)]
dp = [[0]*n for _ in range(m)]
start = MAP[0][0]

dp[0][0] = 1
pq = [(-start, 0, 0)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
while pq:
    num, x, y = heappop(pq)
    if MAP[x][y] == start+1:
        continue

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        print(x, y, nx, ny)
        if not(-1<nx<m and -1<ny<n) or MAP[nx][ny] >= -num:
            continue
        dp[nx][ny] += dp[x][y]
        heappush(pq, ((-MAP[nx][ny], nx, ny)))
    MAP[x][y] = start+1

print(dp[m-1][n-1])
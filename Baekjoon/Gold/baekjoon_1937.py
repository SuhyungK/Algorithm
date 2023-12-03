# 욕심쟁이 판다

import heapq, sys
sys.setrecursionlimit(25001)

def dfs(i, j):
    for ni, nj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
        if ni < 0 or nj < 0 or ni >= n or nj >= n or forest[ni][nj] <= forest[i][j]:
            continue

        if dist[ni][nj]:
            dist[i][j] = max(dist[i][j], dist[ni][nj]+1)
        else:
            dist[i][j] = max(dist[i][j], dfs(ni, nj))
    return dist[i][j]+1


n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * n for _ in range(n) ]
pq = []

for i in range(n):
    for j in range(n):
        heapq.heappush(pq, (forest[i][j], i, j))

while pq:
    x, i, j = heapq.heappop(pq)
    if dist[i][j]:
        continue
    dist[i][j] = max(1, dfs(i, j))

answer = 0
for row in dist:
    answer = max(answer, max(row))

print(answer)
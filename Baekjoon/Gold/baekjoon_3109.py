# 빵집

import sys
input = sys.stdin.readline

def dfs(x, y):
    global way
    visited[x][y] = True
    if y == C - 1:
        way += 1
        return True
    
    for k in range(3):
        nx, ny = x + DIR[k][0], y + DIR[k][1]
        if (nx < 0 or nx >= R or MAP[nx][ny] == 'x' or visited[nx][ny]): continue
        if dfs(nx, ny):
            return True
    # visited[x][y] = False
    return False

R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
DIR = [(-1, 1), (0, 1), (1, 1)]
way = 0

for i in range(R):
    visited[i][0] = True
    dfs(i, 0)

print(way)

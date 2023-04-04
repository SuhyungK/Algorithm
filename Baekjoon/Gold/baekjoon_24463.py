# 미로
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
# .인 경우 미리 @로 바꿔놓기
maze = [list(map(lambda x: '@' if x == '.' else x, input())) for _ in range(N)]

# 가장자리에 있는 입구 '.' 위치 찾기
def start():
    for i in 0, N-1:
        for j in range(M):
            if maze[i][j] == '@':
                return i, j
    for i in range(N):
        for j in 0, M-1:
            if maze[i][j] == '@':
                return i, j

# dfs, 완전탐색, 모든 길을 방문해서 
# 최종적으로 맞는 길의 경우에는 ., 아닌 경우에는 @로 바꿔야함
def dfs(i, j):
    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni, nj = i + di, j + dj
        if not (-1 < ni < N and -1 < nj < M):
            continue
        if maze[ni][nj] == '@':
            maze[ni][nj] = '.'
            if (ni == 0 or ni == N-1) or (nj == 0 or nj == M-1):
                return True
            if dfs(ni, nj):
                maze[ni][nj] = '.'
                return True
            else:
                maze[ni][nj] = '@'

si, sj = start()
maze[si][sj] = '.'
dfs(si, sj)

for row in maze:
    print(''.join(row))

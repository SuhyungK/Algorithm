# 치즈

import sys
sys.stdin = open('input.txt')
from collections import deque

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(queue):
    # 외부 공기 찾기
    next_queue = queue.copy()
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not is_valid(nx, ny) or visited[nx][ny] or cheeze[nx][ny]:
                continue
            next_queue.append((nx, ny))
            queue.append((nx, ny))
            visited[nx][ny] = 1

    # 맞닿은 치즈 찾기
    while next_queue:
        x, y = next_queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not is_valid(nx, ny) or not cheeze[nx][ny]:
                continue
            visited[nx][ny] += 1

    cheeze_queue = deque()
    for x in range(N):
        for y in range(M):
            if cheeze[x][y] and visited[x][y] >= 2:
                cheeze_queue.append((x, y))
                cheeze[x][y] = 0
    # for row in cheeze:
    #     print(*row)
    # print(cheeze_queue)
    return cheeze_queue
            
def is_all_find():
    for row in cheeze:
        if sum(row):
            return False
    return True

N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]

queue = deque([(0, 0)])
out_air = deque()
visited = [[0] * M for _ in range(N)]
dx = (0, 1, -1, 0)
dy = (1, 0, 0, -1)


hour = 0
while not is_all_find():
    queue = bfs(queue)
    hour += 1

print(hour)
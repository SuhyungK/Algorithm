# 백조의 호수

import sys
from collections import deque
input = sys.stdin.readline

# 범위 확인 
def is_valid(x, y, target):
    return 0 <= x < R and 0 <= y < C and lake[x][y] in target

# 특정 queue 를 시작으로 bfs
# target 값을 가지면서 방문처리 배열의 값이 second 가 아니여야 함
def bfs(queue, second, target):
    new_queue = deque()
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not is_valid(nx, ny, target) or visited[nx][ny] == second: # bfs 할 때 한 번 방문한 곳을 두 번 방문하면 안 됨
                continue
            visited[nx][ny] = second
            new_queue.append((nx, ny))
            lake[nx][ny] = "."

    return new_queue

def find(x, y):
    if parent[x][y] != (x, y):
        parent[x][y] = find(*parent[x][y])
    return parent[x][y]

def union(x1, y1, x2, y2):
    x1, y1 = parent[x1][y1]
    x2, y2 = parent[x2][y2]
    
    if (x1, y1) < (x2, y2):
        parent[x2][y2] = (x1, y1)
    else:
        parent[x1][y1] = (x2, y2)

# 집합 연결
def make_set(queue, target):
    for x, y in queue:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not is_valid(nx, ny, target) or find(x, y) == find(nx, ny): # 한 번 방문했던 곳이어도 같은 집합인지 여부는 확인해야 함
                continue
            union(x, y, nx, ny)

R, C = map(int, input().split())
lake = [list(input()) for _ in range(R)]
visited = [[-1] * C for _ in range(R)]
parent = [[(i, j) for j in range(C)] for i in range(R)]
dx = (0, 1, -1, 0)
dy = (1, 0, 0, -1)

# 초기 물 공간의 위치 모두 찾기
second = 0
queue = deque()
swans = []
for i in range(R):
    for j in range(C):
        if lake[i][j] != 'X':
            visited[i][j] = second
            queue.append((i, j))

            if lake[i][j] == 'L':
                swans.append((i, j))

while True:
    # 집합 만들기
    make_set(queue, [".", "L"])

    # 백조들이 만날 수 있는지 확인 -> 같은 집합인가 
    if find(*swans[0]) == find(*swans[1]):
        break

    second += 1
    queue = bfs(queue, second, ["X"])
    
print(second)
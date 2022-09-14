import sys
from collections import deque

def bfs(start):
    q = deque()

    for i in start :
        q.append(i)

    while q:
        y, x = q.popleft()

        for moveY in range(-1, 2, 1):
            for moveX in range(-1, 2, 1):
                dx = x + moveX
                dy = y + moveY

                if 0 <= dx < M and 0 <= dy < N and board[dy][dx] == 0:
                    q.append((dy, dx))
                    board[dy][dx] = board[y][x] + 1
        for b in board:
            print(b)
        print()

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark = []

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 :
            shark.append((i, j))

bfs(shark)

ans = 0
for i in range(N) :
    for j in range(M) :
        ans = max(ans, board[i][j] - 1)

print(ans)

# 확장 게임

from collections import defaultdict

def is_finish():
    return sum(list(castle.values())) != total\
            and any(list(player.values()))

def bfs(queue, p, s):
    global castle
    while queue and s:
        new_queue = []
        for r, c in queue:
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc 
                if 0<=nr<N and 0<=nc<M and board[nr][nc] == '.' and board[nr][nc] != '#':
                    board[nr][nc] = p 
                    new_queue.append((nr, nc))
        queue = new_queue[:]
        castle[p] += len(queue)
        s -= 1

    return queue

N, M, P = map(int, input().split())
S = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
player = defaultdict(list)
castle = defaultdict(int)
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
total = N*M

for i in range(N):
    for j in range(M):
        if board[i][j].isdigit():
            player[board[i][j]].append((i, j))
            castle[board[i][j]] += 1
        if board[i][j] == '#':
            total -= 1

while is_finish():
    for i in range(1, P+1):
        p = str(i)
        if not player[p]:
            continue
        player[p] = bfs(player[p], p, S[i-1])

for i in range(1, P+1):
    print(castle[str(i)], end=' ')
print()
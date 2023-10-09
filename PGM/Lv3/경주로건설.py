def solution(board):
    N = len(board)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pq = [(-500, 0, 0, -1)]
    visited = [[[1e9]*N for _ in range(N)] for _ in range(4)]
    visited[0][0][0], visited[1][0][0], visited[2][0][0], visited[3][0][0] = 0, 0, 0, 0
    while pq:
        cost, x, y, d = heapq.heappop(pq)
        
        if (x, y) == (N-1, N-1):
            return cost
        
        if visited[d][x][y] < cost:
            continue

        for i in range(4):
            nx, ny = x+dirs[i][0], y+dirs[i][1]
            if i == d:
                next_cost = cost+100
            else:
                next_cost = cost+600
            if -1<nx<N and -1<ny<N and board[nx][ny] != 1 and visited[d][nx][ny] >= next_cost:
                visited[d][nx][ny] = next_cost
                heapq.heappush(pq, (next_cost, nx, ny, i))

import heapq

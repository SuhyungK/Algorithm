# 벽 부수고 이동하기2
from collections import deque

N, M, K = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
dr, dc = (1, 0, -1, 0), (0, 1, 0, -1)

def solution():
    visited = [[[0]*(M) for _ in range(N)] for _ in range(K+1)]
    
    queue = deque([(0, 0, K)])
    visited[K][0][0] = 1

    while queue:
        r, c, k = queue.popleft()
        if r == N-1 and c == M-1:
            return visited[k][r][c]
        
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            
            if MAP[r][c] == 1 and k and not visited[k-1][nr][nc]:
                visited[k-1][nr][nc] = visited[k][r][c]+1
                queue.append((nr, nc, k-1))
            elif MAP[r][c] == 0 and not visited[k][nr][nc]:
                visited[k][nr][nc] = visited[k][r][c]+1
                queue.append((nr, nc, k))
    return -1
    
print(solution())
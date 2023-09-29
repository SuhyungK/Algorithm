def solution(maps):
    q = [(0, 0)]
    
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
    
    visited[0][0] = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m or visited[nx][ny] or not maps[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            if (nx, ny) == (n-1, m-1):
                return visited[nx][ny]
            q.append((nx, ny))
    return -1
        
# 보급로

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dis = [list(map(int, input())) for _ in range(N)]
    visit = [[N*N*9] * N for _ in range(N)]
    visit[0][0] = 0
    queue = [(0, 0)]
 
    while queue:
        x, y = queue.pop(0)
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] > visit[x][y] + dis[nx][ny]:
                visit[nx][ny] = visit[x][y] + dis[nx][ny]
                queue.append((nx, ny))
 
    print(f'#{tc}', visit[N-1][N-1])
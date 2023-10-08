# 농장 관리

def bfs(_i, _j, x):
    flag = True
    visited[_i][_j] = True
    queue = [(_i, _j)]
    while queue:
        i, j = queue.pop(0)
        for di, dj in dij:
            ni, nj = i+di, j+dj 
            if -1<ni<N and -1<nj<M:
                if arr[ni][nj] > arr[i][j]:
                    flag = False
                elif not visited[ni][nj] and arr[ni][nj] == x:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    return flag

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dij = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

cnt = 0 
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += bfs(i, j, arr[i][j])
print(cnt)
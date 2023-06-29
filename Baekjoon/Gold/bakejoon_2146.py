# 다리 만들기

# 각각의 섬에 번호 붙이기
def findLand(x, y, z):
    global land
    visited[x][y] = z
    land[z] = [(x, y, 0)]
    q = [(x, y)]

    while q:
        x, y = q.pop(0)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or ny<0 or nx>=N or ny>=N or not arr[nx][ny] or visited[nx][ny]:
                continue

            visited[nx][ny] = z
            land[z].append((nx, ny, 0))
            q.append((nx, ny))

# 각 섬에 땅에 대해서 땅에선 0을 찾고 0에선 다른 땅을 찾는 거
def putBridge(n, q):
    while q:
        x, y, cnt = q.pop(0)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or ny<0 or nx>=N or ny>=N or visited[nx][ny] == n:
                continue
            
            # 방문한 곳이 바다라면 q에 추가
            if not arr[nx][ny]:
                visited[nx][ny] = n
                q.append((nx, ny, cnt+1))
        
            # 방문한 곳이 바다가 아니라면 새로운 육지이니까 
            elif arr[nx][ny]:
                return cnt
            

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
land = {}
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

z = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            findLand(i, j, z)
            z += 1

minLen = N*N
for num, lst in land.items():
    minLen = min(minLen, putBridge(num, lst))

print(minLen)
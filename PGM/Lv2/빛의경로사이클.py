# 빛의 경로 사이클

def solution(grid):
    n, m = len(grid), len(grid[0])
    visited = [[[False]*m for _ in range(n)] for _ in range(4)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 상 우 하 좌
        
    
    for row in visited:
        print(row)

    ans = []
    for k in range(4):
        for x in range(n):
            for y in range(m):
                print(visited[k][x][y])
                if visited[k][x][y]:
                    continue
                    
                cnt = 0
                while not visited[k][x][y]:
                    print(k, x, y)
                    visited[k][x][y] = True
                    x = (x+dx[k])%n
                    y = (y+dy[k])%m
                    
                    if grid[x][y] == "L":
                        k = (k-1)%4
                    elif grid[x][y] == "R":
                        k = (k+1)%4
                    cnt += 1
                ans.append(cnt)
    
    ans.sort()
    return ans
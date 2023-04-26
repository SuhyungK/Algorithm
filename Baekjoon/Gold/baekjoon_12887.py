# 경로 게임

n = int(input())
route = [list(input()) for _ in range(2)]

res = 2*n - sum(route, []).count('#')

def bfs(r, c):
    cnt = 0
    while 1:
        cnt += 1
        if c == n-1:
            return cnt
        
        if c+1 < n and route[r][c+1] == '.':
            c += 1
        elif r == 0:
            r += 1
        elif r == 1:
            r -= 1

min_cnt = 2*n    
if route[0][0] == '.':
    min_cnt = min(min_cnt, bfs(0, 0))

if route[1][0] == '.':
    min_cnt = min(min_cnt, bfs(1, 0))

print(res - min_cnt)
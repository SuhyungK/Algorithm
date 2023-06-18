# 사다리 조작
import sys

def check():
    s = 0
    while s < N-1:
        t = s
        for i in range(H):
            if -1<t-1 and ladder[i][t-1]:
                t -= 1
            elif ladder[i][t]:
                t += 1
        
        if t != s:
            return False
        s += 1
    return True

def dfs(cnt, x, y):
    global minCnt
    print(x, y)
    if minCnt <= cnt:
        return 
    
    if check():
        minCnt = min(minCnt, cnt)
        return 
    
    if cnt == 3:
        return 
    
    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N-1):
            if ladder[i][j] == 0:
                ladder[i][j] = 1
                dfs(cnt+1, i, j+2)
                ladder[i][j] = 0
            else:
                dfs(cnt, i, j+2)

N, M, H = map(int, input().split())
ladder = [[0]*N for _ in range(H)]
minCnt = 4

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a-1][b-1] = 1

dfs(0, 0, 0)
print(-1 if minCnt == 4 else minCnt)
import sys
sys.stdin = open('test.txt', 'r')

def dfs(r, c, idx, cnt):
    global maxV
    if idx == 4:
        return
    elif idx == 3 and (r, c) == (i, j):
        if maxV < cnt:
            maxV = cnt
        return

    dr, dc = r + dx[idx], c + dy[idx]
    if -1 < dr < N and -1 < dc < N:
        if dessert.get(arr[dr][dc]):
            return
        else:
            dessert[arr[dr][dc]] = 1
            dfs(dr, dc, idx, cnt+1)
            dfs(dr, dc, idx+1, cnt+1)
    else:
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    maxV = -1
    for i in range(N-2):
        for j in range(1, N-1):
            dessert = {}
            dfs(i, j, 0, 0)
                
    print(f'#{tc}', maxV)
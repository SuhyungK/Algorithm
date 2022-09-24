import sys
sys.stdin = open('test.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    micro = {}

    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    dir = [0, 2, 1, 4, 3]

    for k in range(K):
        micro[k] = list(map(int, input().split()))
    
    while M:
        arr = {}        
        for idx in range(K):
            mir = micro[idx]
            y, x, n, d = mir
            if n == 0:
                continue
            
            ny, nx = y + dy[d], x + dx[d]
            mir[0] = ny
            mir[1] = nx
            if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                mir[2] //= 2
                mir[3] = dir[d]
            
            if arr.get((ny, nx)):
                pre_idx, pre_n = arr[(ny, nx)]
                if pre_n < n:
                    mir[2] += micro[pre_idx][2]
                    micro[pre_idx][2] = 0
                    arr[(ny, nx)] = (idx, n)   
                else:
                    micro[pre_idx][2] += n
                    mir[2] = 0
            else:
                arr[(ny, nx)] = (idx, n)
        M -= 1

    res = 0
    for i in range(K):
        res += micro[i][2]

    print(f'#{tc}', res)

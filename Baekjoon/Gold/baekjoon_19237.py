# 어른 상어

def scent_spread():
    global scent
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                continue
            scent[i][j] = [arr[i][j], K]

def find_next(i, j, n, dir):
    for k in dir:
        ni = i+DIR[k][0]
        nj = j+DIR[k][1]
        if -1<ni<N and -1<nj<N and not scent[ni][nj][1]: 
            return ni, nj, k-1
        
    for k in dir:
        ni = i+DIR[k][0]
        nj = j+DIR[k][1]
        if -1<ni<N and -1<nj<N and scent[ni][nj][0] == n:
            return ni, nj, k-1
    
    return 0, 0, 0
        
def move(arr):
    global M
    tmp = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                continue
            n = arr[i][j] # 상어의 번호
            d = SHARK_INFO[n] # 상어의 방향
            dir = PRIORITY[4*(n-1)+d] # 우선순위 
            
            ni, nj, new_d = find_next(i, j, n, dir)
            if not tmp[ni][nj]:
                tmp[ni][nj] = n 
            elif tmp[ni][nj] > n:
                M -= 1
                tmp[ni][nj] = n 
            elif tmp[ni][nj] < n: 
                M -= 1            
            SHARK_INFO[n] = new_d

    return tmp

def scent_disappear():
    global scent 
    for i in range(N):
        for j in range(N):
            if not scent[i][j][1]:
                continue
            scent[i][j][1] -= 1
            if scent[i][j][1] == 0:
                scent[i][j] = [0, 0]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
SHARK_INFO = [0]+list(map(lambda x: int(x)-1, input().split()))
PRIORITY = [list(map(int, input().split())) for _ in range(4*M)]
DIR = [(-1, -1), (-1, 0), (1, 0), (0, -1), (0, 1)]
scent = [[[0, 0] for _ in range(N)] for _ in range(N)]

sec = 0
while M >1:
    if sec >= 1000:
        sec = -1
        break
    
    scent_spread()
    arr = move(arr)
    scent_disappear()
    sec += 1

print(sec)
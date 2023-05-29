# 감시 

def cctv(c, n, t=1):
    cctvs, i = [], 0
    while i < n:
        tmp, j = [], 0
        while j < c:
            tmp.append(dirs[(i+j*t)%4])
            j += 1
        cctvs.append(tmp)
        i += 1

    return cctvs

# cctv들의 위치랑 번호 찾아서 배열로 반환
def cctv_wall():
    ctv, walls = [], 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if 0<arr[i][j]<6:
                ctv.append((arr[i][j], i, j))
            elif arr[i][j] == 6:
                walls += 1
    return ctv, walls, len(ctv)+walls

def sol(k, v, cnt):
    global max_cnt
    if k == len(ctvs):
        max_cnt = max(max_cnt, cnt)
        # print(max_cnt)
        # for row in v:
        #     print(*row)
        # print()
        return 
    
    num, i, j = ctvs[k]
    for dir in ctv_num[num]:
        c = 0
        tmp_v = [row[:] for row in v]
        for di, dj in dir:
            si, sj = i+di, j+dj
            while (a:=arr[si][sj])!=6:
                if a == 0 and v[si][sj] != '#':
                    c += 1
                    v[si][sj] = '#'
                si += di
                sj += dj
        sol(k+1, v, cnt+c)
        v = [row[:] for row in tmp_v]


N, M = map(int, input().split())
arr = [[6]*(M+2)] +[[6]+list(map(int, input().split()))+[6] for _ in range(N)]+[[6]*(M+2)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ctv_num = {
    1: cctv(1, 4), 
    2: cctv(2, 2, 2), 
    3: cctv(2, 4),
    4: cctv(3, 4), 
    5: cctv(4, 1)
}

visit = [[0]*(M+2) for _ in range(N+2)]
ctvs, walls, ctvwall = cctv_wall()
max_cnt = 0


sol(0, visit, 0)
print(N*M-ctvwall-max_cnt)
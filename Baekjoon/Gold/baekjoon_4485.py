# 녹색 옷 입은 애가 젤다지?

import heapq

def sol(N):
    cave = [list(map(int, input().split())) for _ in range(N)]
    arr = [[100000]*N for _ in range(N)]
    arr[0][0] = cave[0][0]
    pq = [(cave[0][0], 0, 0)]
    di, dj = (0, 1, 0, -1), (1, 0, -1, 0)
    
    while pq:
        rp, i, j = heapq.heappop(pq)
        if arr[i][j] < rp:
            continue

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if ni<0 or nj<0 or ni>=N or nj>=N:
                continue
                
            if arr[ni][nj] > rp + cave[ni][nj]:
                arr[ni][nj] = rp + cave[ni][nj]
                if ni == N-1 and nj == N-1:
                    return arr[ni][nj]
                heapq.heappush(pq, (arr[ni][nj], ni, nj))

pb = 1
while True:
    n = int(input())
    if not n:
        break
    print(f'Problem {pb}: {sol(n)}')
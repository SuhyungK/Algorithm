# 감시 

def watch(i, j, *cctv):
    global watch_spot
    spot_list = []
    for dir in cctv:
        spot = set()
        for d in dir:
            ni, nj = i+di[d], j+dj[d]
            while arr[ni][nj] != 6:
                if not arr[ni][nj]:
                    spot.add((ni, nj))
                ni += di[d]
                nj += dj[d]
        spot_list.append(spot)
    
    watch_spot[(i, j)] = spot_list
                
def sol(i, spots, K):
    global blind
    if i == K:
        blind = min(blind, zero_spot-len(spots))
        return 
    
    for watch_list in watch_spot[cctvs[i]]:
        sol(i+1, spots | watch_list, K)

N, M = map(int, input().split())
arr = [[6]*(M+2)] +[[6]+list(map(int, input().split()))+[6] for _ in range(N)]+[[6]*(M+2)]
di, dj = (-1, 0, 1, 0), (0, 1, 0, -1)

zero_spot, blind = 0, 1e13
watch_spot = dict()
for i in range(1, N+1):
    for j in range(1, M+1):
        a = arr[i][j]
        if a == 0:
            zero_spot += 1
        elif a == 1:
            watch(i, j, [0], [1], [2], [3])
        elif a == 2:
            watch(i, j, [0, 2], [1, 3])
        elif a == 3:
            watch(i, j, [0, 1], [1, 2], [2, 3], [3, 0])
        elif a == 4:
            watch(i, j, [0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1])
        elif a == 5:
            watch(i, j, [0, 1, 2, 3])

cctvs = list(watch_spot.keys())

sol(0, set(), len(cctvs))
print(blind)
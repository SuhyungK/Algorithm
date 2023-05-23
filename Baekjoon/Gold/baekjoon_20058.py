# 마법사 상어와 파이어스톰
import sys
sys.stdin = open('input.txt')

# 90도 회전
def rotate_90(arr):
    return list(map(list, zip(*arr[::-1])))

def devide(l, p):
    k = 0
    while k < p*p:
        n, m = k//p*l, k%p*l
        tmp = rotate_90([row[m:m+l] for row in ices[n:n+l]])
        for i in range(l):
            for j in range(l):
                ices[n+i][j+m] = tmp[i][j]
        
        k += 1

# 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
def melt(ices):
    next_ices = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            ice_here = 0
            next_ices[y][x] = ices[y][x]
            if y+1<N and ices[y+1][x]:
                ice_here += 1
            if x+1<N and ices[y][x+1]:
                ice_here += 1
            if -1<y-1 and ices[y-1][x]:
                ice_here += 1
            if -1<x-1 and ices[y][x-1]:
                ice_here += 1
            if ice_here < 3 and ices[y][x] > 0:
                next_ices[y][x] -= 1
    return next_ices
            
def bfs(y, x):
    visit[y][x] = 1
    cnt = 1
    q = [(y, x)]
    while q:
        y, x = q.pop(0)
        if y+1<N and ices[y+1][x] and not visit[y+1][x]:
            visit[y+1][x] = 1
            cnt += 1
            q.append((y+1, x))
        if x+1<N and ices[y][x+1] and not visit[y][x+1]:
            visit[y][x+1] = 1
            cnt += 1
            q.append((y, x+1))
        if -1<y-1 and ices[y-1][x] and not visit[y-1][x]:
            visit[y-1][x] = 1
            cnt += 1
            q.append((y-1, x))
        if -1<x-1 and ices[y][x-1] and not visit[y][x-1]:
            visit[y][x-1] = 1
            cnt += 1
            q.append((y, x-1))
    return cnt

nn, Q = map(int, input().split())
N = 2**nn
ices = [list(map(int, input().split())) for _ in range(N)]
L = list(map(lambda x: 2**int(x), input().split()))
visit = [[0]*N for _ in range(N)]

for l in L:
    devide(l, N//l)
    ices = melt(ices)

total_ice, big_cnt = 0, 0
for i in range(N):
    for j in range(N):
        total_ice += ices[i][j] 
        if ices[i][j] and visit[i][j] == 0:
            big_cnt = max(big_cnt, bfs(i, j))

print(total_ice)
print(big_cnt)
# arr = [[1, 2, 3, 4], [9, 10, 11, 12], [17, 18, 19, 20], [25, 26, 27, 28]]
# # rotate_arr = list(map(list, zip(*arr[::-1]))) 
# # for row in rotate_arr:
# #     print(*row)

# for row in arr:
#     print(row)
# tmp = [row[0:2] for row in arr[0:2]]
# print(tmp)

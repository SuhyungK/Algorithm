# 마법사 상어와 토네이도

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def tornado(arr, d, y, x):
    global total_sand, ans_sand
    dy, dx = dir[d%4]
    if dx == 0:
        dxy_lst = (dy*2, 0), (dy, 1), (dy, -1), (dy*-1, 1), (dy*-1, -1), (0, -1), (0, 1), (0, -2), (0, 2)
    else:
        dxy_lst = (0, dx*2), (1, dx), (-1, dx), (1, dx*-1), (-1, dx*-1), (-1, 0), (1, 0), (-2, 0), (2, 0)
    
    NOW_SAND = alpha = arr[y][x]
    for i in range(9):
        dyy, dxx = dxy_lst[i]
        ny, nx = y+dyy, x+dxx
        tmp = int(NOW_SAND * RATIO[i])
        alpha -= tmp
        if -1<ny<N and -1<nx<N:
            arr[ny][nx] += tmp
        else: ans_sand += tmp

    if -1<y+dy<N and -1<x+dx<N:
        arr[y+dy][x+dx] += alpha
    else:
        ans_sand += alpha

    arr[y][x] = 0

def main():
    x = y = N//2
    u, v, d = 1, -1, 0
    while 1:
        if u == N:
            break
        for _ in range(u):
            x += v
            tornado(arr, d, y, x)
        v *= -1
        d += 1
        
        for _ in range(u):
            y += v
            tornado(arr, d, y, x)
        u += 1
        d += 1
    
    for _ in range(N-1):
        x -= 1
        tornado(arr, d, y, x)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = (0, -1), (1, 0), (0, 1), (-1, 0)
RATIO = [0.05, 0.1, 0.1, 0.01, 0.01, 0.07, 0.07, 0.02, 0.02]
ans_sand = 0
main()
print(ans_sand)
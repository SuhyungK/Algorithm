# 미세먼지 안녕!

def FIND_DUST(dusts, R, C):
    dust_lst = {}
    for i in range(R):
        for j in range(C):
            if (dust_amount:=dusts[i][j]) > 0:
                dust_lst[(i, j)] = dust_amount

    return dust_lst

def FIND_CLENADER(dusts, R):
    for i in range(R):
        if dusts[i][0] == -1:
            return i, i+1

def diffusion(dusts, R, C):
    new_dusts = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 공기청정기 피하기
            if dusts[i][j] == -1:
                new_dusts[i][j] = -1
                continue

            # 굳이 미세먼지가 없는 부분은 확인하지 않음 왜냐면 많이 반복될수록 미세먼지 없는 칸이 없으므로..
            dust = dusts[i][j]
            diffusion_dust, diffusion_area = dust // 5, 0
            if i+1 < R and dusts[i+1][j] != -1:
                new_dusts[i+1][j] += diffusion_dust
                diffusion_area += 1
            if j+1 < C and dusts[i][j+1] != -1:
                new_dusts[i][j+1] += diffusion_dust
                diffusion_area += 1
            if i-1 > -1 and dusts[i-1][j] != -1:
                new_dusts[i-1][j] += diffusion_dust
                diffusion_area += 1
            if j-1 > -1 and dusts[i][j-1] != -1:
                new_dusts[i][j-1] += diffusion_dust
                diffusion_area += 1
            new_dusts[i][j] += (dust - diffusion_dust * diffusion_area)
    
    return new_dusts
                
def rotate(dusts, R, C):
    # 1열에 있는 미세먼지 이동(공기 청정기 바로 위쪽은 빨려들어가기 때문에 제외)
    for i in range(TOP_ROW-2, -1, -1):
        dusts[i+1][0] = dusts[i][0]
    # 1행에 있는 미세먼지 이동
    for j in range(1, C):
        dusts[0][j-1] = dusts[0][j]
    # C-1열에 있는 미세먼지 이동
    for i in range(1, TOP_ROW+1):
        dusts[i-1][C-1] = dusts[i][C-1]
    # TOP_ROW행에 있는 미세먼지 이동(0열에 있는 공기청정기는 이동할 필요 없음)
    for j in range(C-2, 0, -1):
        dusts[TOP_ROW][j+1] = dusts[TOP_ROW][j]
    dusts[TOP_ROW][1] = 0

    for i in range(UNDER_ROW+2, R):
        dusts[i-1][0] = dusts[i][0]
    for j in range(1, C):
        dusts[R-1][j-1] = dusts[R-1][j]
    for i in range(R-2, UNDER_ROW-1, -1):
        dusts[i+1][C-1] = dusts[i][C-1]
    for j in range(C-2, 0, -1):
        dusts[UNDER_ROW][j+1] = dusts[UNDER_ROW][j]
    dusts[UNDER_ROW][1] = 0

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
dusts = [list(map(int, input().split())) for _ in range(R)]

TOP_ROW, UNDER_ROW = FIND_CLENADER(dusts, R)

t = 0
while t < T:
    dusts = diffusion(dusts, R, C)
    rotate(dusts, R, C)
    t += 1

answer = 2
for row in dusts:
    answer += sum(row)
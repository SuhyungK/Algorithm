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

def speard_dust(dusts, R, C, dust_lst, new_dusts):
    dust_lst = FIND_DUST(dusts, R, C)

    for dust, amount in dust_lst.items():
        r, c = dust
        to_amount = amount // 5
        if to_amount > 0:
            for d in range(4):
                dr, dc = SPREAD_DIR[d]
                nr, nc = r+dr, c+dc
                if -1 < nr < R and -1 < nc < C and dusts[nr][nc] != -1: 
                    new_dusts[nr][nc] += to_amount
                    amount -= to_amount
            
        new_dusts[r][c] += amount

    return new_dusts

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
dusts = [list(map(int, input().split())) for _ in range(R)]

TOP_CLEAN = ((-1, 0), (0, 1), (1, 0), (0, -1))
DOWN_CELAN = ((1, 0), (0, 1), (-1, 0), (0, -1))
SPREAD_DIR = ((1, 0), (0, 1), (-1, 0), (0, -1))

TOP_BOUNDARY, UNDER_BOUNDARY = FIND_CLENADER(dusts, R)

dust_lst = FIND_DUST(dusts, R, C)
for _ in range(T):
    new_dusts = [[0] * C for _ in range(R)]
    new_dusts[TOP_BOUNDARY][0] = -1
    new_dusts[UNDER_BOUNDARY][0] = -1

    dusts = speard_dust(dusts, R, C, dust_lst, new_dusts)
    
    # TOP_CLEAN
    START_ROW, START_COL = TOP_BOUNDARY, 0
    for d in range(4):
        dr, dc = TOP_CLEAN[d]
        while -1 < START_ROW+dr <= TOP_BOUNDARY and -1 < START_COL+dc < C:
            dusts[START_ROW][START_COL], dusts[START_ROW+dr][START_COL+dc] = dusts[START_ROW+dr][START_COL+dc], dusts[START_ROW][START_COL]
            START_ROW += dr
            START_COL += dc
    dusts[TOP_BOUNDARY][1] = 0

    # UNDER_CLEAN
    START_ROW, START_COL = UNDER_BOUNDARY, 0
    for d in range(4):
        dr, dc = DOWN_CELAN[d]
        while UNDER_BOUNDARY <= START_ROW+dr < R and -1 < START_COL+dc < C:
            dusts[START_ROW][START_COL], dusts[START_ROW+dr][START_COL+dc] = dusts[START_ROW+dr][START_COL+dc], dusts[START_ROW][START_COL]
            START_ROW += dr
            START_COL += dc
    dusts[UNDER_BOUNDARY][1] = 0
    dust_lst = FIND_DUST(dusts, R, C)

print(sum(dust_lst.values()))
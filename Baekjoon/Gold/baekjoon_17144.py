# 미세먼지 안녕!

def FIND_DUST(dusts, R, C):
    dust_lst = []
    for i in range(R):
        for j in range(C):
            if dusts[i][j]:
                dust_lst.append((i, j))

    return dust_lst

def FIND_CLENADER(dusts, R):
    for i in range(R):
        if dusts[i][0] == -1:
            return (i, 0), (i+1, 0)
        
def dust_spread(dusts):

    pass

R, C, T = map(int, input().split())
dusts = [list(map(int, input().split())) for _ in range(R)]

TOP_CLEAN = ((-1, 0), (0, 1), (1, 0), (0, -1))
DOWN_CELAN = ((1, 0), (0, 1), (-1, 0), (0, -1))
SPREAD_DIR = ((1, 0), (0, 1), (-1, 0), (0, -1))

dust_lst = FIND_DUST(dusts, R, C)
cleaner = FIND_CLENADER(dusts, R)

for dust in dust_lst:
    r, c = dust
    amount = dusts[r][c]
    to_amount = amount // 5
    if to_amount // 5:
        for d in range(4):
            dr, dc = SPREAD_DIR[d]
            nr, nc = r+dr, c+dc
            if -1 < nr < R and -1 < nc < C:
                dusts[nr][nc] += to_amount
    else:
        pass

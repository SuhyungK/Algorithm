def bfs():
    while 1:
        newWater = []
        print('에러')
        for wr, wc in water:
            for i in range(4):
                nr, nc = wr + dr[i], wc + dr[i]
                if -1 < nr < r and -1 < nc < c and fst[nr][nc] == '.':
                    fst[nr][nc] = '*'
                    newWater.append((nr, nc))
        
        print('에러')
        newbb = []
        for br, bc in bb:
            for i in range(4):
                nr, nc = br + dr[i], bc + dr[i]
                if -1 < nr < r and -1 < nc < c and fst[nr][nc] not in ['*', 'X']:
                    if fst[nr][nc] == 'D':
                        return fst[br][bc]
                    else:
                        fst[nr][nc] = fst[br][bc] + 1
                    newbb.append((nr, nc))
        water = newWater
        bb = newbb

    return 'KAKTUS'

r, c = map(int, input().split())
fst = [list(input()) for _ in range(r)]

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

water, bb = [], []
for i in range(r):
    for j in range(c):
        if fst[i][j] == '*':
            water.append([i, j])
        elif fst[i][j] == 'S':
            bb = [[i, j]]
            fst[i][j] = 1

bfs()
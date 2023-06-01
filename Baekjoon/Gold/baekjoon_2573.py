# 빙산

def melt(i, j, t):
    cnt = 0
    if -1<i-1 and not iceberg[i-1][j]:
        cnt += 1
    if -1<j-1 and not iceberg[i][j-1]:
        cnt += 1
    if i+1<N and not iceberg[i+1][j]:
        cnt += 1
    if j+1<M and not iceberg[i][j+1]:
        cnt += 1
    
    if t >= cnt:
        return t-cnt
    return 0

def _init():
    q = []
    for i in range(N):
        for j in range(M):
            if iceberg[i][j]:
                q.append((i, j))
    return q

def bfs(i, j, year):
    global visit
    _q = [(i, j)]
    _new_q = []
    while _q:
        i, j = _q.pop(0)

        for ni, nj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if iceberg[ni][nj] and visit[ni][nj] != year:
                visit[ni][nj] = year
                _new_q.append((ni, nj, melt(ni, nj, iceberg[ni][nj])))
                _q.append((ni, nj))

    return _new_q

def sol():
    global iceberg
    q = _init()
    year = 1
    
    while True:
        new_q, is_lump = [], False
        for y, x in q:
            if visit[y][x] != year:
                if is_lump:
                    return year-1
                new_q.extend(bfs(y, x, year))

                is_lump = True

        q = []
        for y, x, t in new_q:
            if t:
                q.append((y, x))
                iceberg[y][x] = t
            else: iceberg[y][x] = 0

        if not q: return 0
        year += 1

if __name__ == '__main__':
    N, M = map(int, input().split())
    iceberg = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    print(sol())
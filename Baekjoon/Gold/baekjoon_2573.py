# 빙산

def melt(i, j, t):
    cnt = 0
    if -1<i-1 and not iceberg[i-1][j]:
        cnt += 1
    if -1<j-1 and not iceberg[i][j-1]:
        cnt += 1
    if i+1<N and iceberg[i+1][j]:
        cnt += 1
    if j+1<M and iceberg[i][j+1]:
        cnt += 1
    
    if t >= cnt:
        return t-cnt
    return 0

def bfs(visit, si, sj):
    q = [(si, sj)]

    while q:
        si, sj = q.pop(0)
        for ni, nj in (si+1, sj), (si-1, sj), (si, sj+1), (si, sj-1):
            if ni<0 or nj<0 or ni>=N or nj>=M:
                continue
            if not visit[ni][nj] and iceberg[ni][nj]:
                visit[ni][nj] = melt(ni, nj, iceberg[ni][nj])
                q.append((ni, nj))

    return visit

def sol():
    year = 0
    while True:
        is_lump = False
        visit = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if iceberg[i][j] and not visit[i][j]:
                    if is_lump:
                        return year
                    visit = bfs(visit, i, j)
                    is_lump = True
        if not is_lump:
            return 0
        year += 1

if __name__ == '__main__':
    N, M = map(int, input().split())
    iceberg = [list(map(int, input().split())) for _ in range(N)]
    print(sol())
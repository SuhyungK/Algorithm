# G5 도넛 행성

N, M = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if planet[i][j] == 0:
            pass

def find_forest(r, c):
    planet[r][c] = 1
    q = [(r, c)]
    while q:
        r, c = q.pop(0)

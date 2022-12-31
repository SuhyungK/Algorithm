N, M = map(int, input().split())
Hx, Hy = map(lambda x: int(x) - 1, input().split())
Ex, Ey = map(lambda x: int(x) - 1, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[[0, 0] for _ in range(M)] for _ in range(N)]

def bfs():
    q = [(Hx, Hy, arr[Hx][Hy])]
    v[Hx][Hy][0] = 1
    while q:
        r, c, wall = q.pop(0)

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if -1 < nr < N and -1 < nc < M and v[nr][nc][wall] == 0:
                if (nr, nc) == (Ex, Ey):
                    return v[r][c][wall]
                if wall == 0 and arr[nr][nc]:
                    v[nr][nc][1] = v[r][c][wall] + 1
                    q.append((nr, nc, 1))
                elif arr[nr][nc] == 0:
                    v[nr][nc][wall] = v[r][c][wall] + 1
                    q.append((nr, nc, wall))
    return -1 

print(bfs())
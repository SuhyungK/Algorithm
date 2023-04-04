# 인구이동

def bfs():
    flag = False
    for i in range(N):
        for j in range(N):
            if visit[i][j] == time -1:
                unn = {}
                q = [(i, j)]
                while q:
                    r, c = q.pop(0)
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if -1 < nr < N and -1 < nc < N and visit[nr][nc] != time:
                            if L <= abs(arr[nr][nc] - arr[r][c]) <= R:
                                visit[nr][nc] = time
                                q.append((nr, nc))
                                unn[(nr, nc)] = arr[nr][nc]
                if unn:
                    flag = True
                    l = len(unn.keys())
                    ppl = sum(unn.values()) // l
                    for kr, kv in list(unn.keys()):
                        arr[kr][kv] = ppl
    return flag


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[-1] * N for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

time = 0
while 1:
    if not bfs():
        break
    time += 1

print(time)
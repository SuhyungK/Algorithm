# 적록색약

def find_group(r, c, t, v):
    q = [(r, c)]
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 > nr or nr >= N or 0 > nc or nc >= N:
                continue
            if visit[nr][nc] == v and arr[nr][nc] in group[t]:
                visit[nr][nc] = v + 1
                q.append((nr, nc))

N = int(input())
arr = [list(input()) for _ in range(N)]

visit = [[0] * N for _ in range(N)]
group = {'R': 'R', 'G': 'G', 'B': 'B'}
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

cnt_1 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            visit[i][j] = 1
            cnt_1 += 1
            find_group(i, j, arr[i][j], 0)

cnt_2 = 0
group['R'] = group['G'] = ('R', 'G')
for i in range(N):
    for j in range(N):
        if visit[i][j] == 1:
            cnt_2 += 1
            visit[i][j] = 2
            find_group(i, j, arr[i][j], 1)

print(cnt_1, cnt_2)
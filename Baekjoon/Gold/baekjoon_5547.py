def bfs(l: tuple):
    global d
    r, c = l
    k = arr[r][c]
    if k == 0:
        q = [(r, c)]
        arr[r][c] = 2
        while q:
            r, c = q.pop(0)
            for dr, dc in dir[r%2]:
                nr, nc = r + dr, c + dc
                if -1 < nr < H and -1 < nc < W:
                    if arr[nr][nc] == 0:
                        q.append((nr, nc))
                        arr[nr][nc] = 2
                    elif arr[nr][nc] == 1:
                        d += 1
    elif k == 1:
        for dr, dc in dir[r%2]:
            if not(-1 < (nr:=r + dr) < H and -1 < (nc:=c + dc) < W):
                d += 1

W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
dir = {
    0: ((0, -1), (1, -1), (-1, 0), (1, 0), (1, 1), (0, 1)),
    1: ((-1, -1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1))
}
d = 0

lst = []
for se in 0, -1:
    for w in range(W):
        lst.append((H-1 if se == -1 else se, w))
    for h in range(H):
        lst.append((h, W-1 if se == -1 else se))

lst = sorted(set(lst))
for l in lst:
    bfs(l)

print(d)
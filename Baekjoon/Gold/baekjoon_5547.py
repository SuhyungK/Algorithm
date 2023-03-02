# -------------------- dfs ---------------------
W, H = map(int, input().split())
arr = [[0] * (W+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(H)] + [[0] * (W+2)]
dir = {
    0: ((-1, -1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1)), 
    1: ((0, -1), (1, -1), (-1, 0), (1, 0), (1, 1), (0, 1))
}

def dfs():
    ans = 0
    stk = [(0, 0)]
    arr[0][0] = 2
    while stk:
        r, c = stk.pop()
        for dc, dr in dir[r%2]:
            nr, nc = r + dr, c + dc
            if -1 < nr < H + 2 and -1 < nc < W + 2:
                if arr[nr][nc] == 1:
                    ans += 1
                elif arr[nr][nc] == 0:
                    stk.append((nr, nc))
                    arr[nr][nc] = 2

    return ans

print(dfs())


# ---------------------- bfs -------------------------

# G4 일루미네이션
def bfs(l: tuple):
    global d
    r, c = l
    k = arr[r][c]
    if k == 0:
        q = [(r, c)]
        arr[r][c] = 2
        while q:
            r, c = q.pop(0)
            for dc, dr in dir[r%2]:
                nr, nc = r + dr, c + dc
                if -1 < nr < H and -1 < nc < W:
                    if arr[nr][nc] == 0:
                        q.append((nr, nc))
                        arr[nr][nc] = 2
                    elif arr[nr][nc] == 1:
                        d += 1
            # print(r, c, d)
    elif k == 1:
        for dc, dr in dir[r%2]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= H or nc < 0 or nc >= W:
                d += 1

W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
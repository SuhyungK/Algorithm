def move():
    for i in range(1, 17):
        if not loc.get(i):
            continue
        x, y = loc[i]
        n, d = score_dir[(x, y)]
        for i in range(8):
            nx, ny = x+dx[(d+i)%8], y+dy[(d+i)%8]
            if nx<0 or ny<0 or nx>3 or ny>3 or score_dir[(nx, ny)][0]<0:
                continue
            score_dir[(nx, ny)], score_dir[(x, y)] = score_dir[(x, y)], score_dir[(nx, ny)]
            break

def revert():
    for i in range(16, 0, -1):
        if not loc.get(i):
            continue
        x, y = loc[i]
        n, d = score_dir[(x, y)]
        d += 4
        for i in range(8):
            nx, ny = x+dx[(d+i)%8], y+dy[(d+i)%8]
            if nx<0 or ny<0 or nx>3 or ny>3 or score_dir[(nx, ny)][0]<0:
                continue
            score_dir[(nx, ny)], score_dir[(x, y)] = score_dir[(x, y)], score_dir[(nx, ny)]
            break

def shark_move(x, y, s): # 상어 이동, (x, y) 상어의 위치
    pass


dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)
loc = {}
score_dir = {}
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        n, d = row[2*j:2*j+2]
        loc[n] = [i, j]
        score_dir[(i, j)] = [n, d-1]
# print(loc)
# print(score_dir)

move()
print(score_dir)
revert()
print(score_dir)
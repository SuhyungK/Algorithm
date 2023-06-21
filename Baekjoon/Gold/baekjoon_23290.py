# 마법사 상어와 복제


# 물고기 이동
def fishMove(x, y, d):
    nx, ny, _d = x+dx[d], y+dy[d], d
    while (nx<0 or ny<0 or nx>3 or ny>3) or smell.get((nx, ny)) or (nx, ny) == (sx, sy):
        _d = (_d-1)%8
        if d == _d:
            return x, y, _d
        nx, ny = x+dx[_d], y+dy[_d]
    return nx, ny, _d

# 상어의 이동
def sharkMove(x, y, cnt, lst):
    global ans, sx, sy
    if len(lst) == 3:
        if ans > (-cnt, lst):
            ans = (-cnt, lst)
        return 
    
    if x-1>-1:
        if not visited[x-1][y]:
            visited[x-1][y] = True
            sharkMove(x-1, y, cnt+sum(new_fish[x-1][y].values()), lst+[1])
            visited[x-1][y] = False
        else:
            sharkMove(x-1, y, cnt, lst+[1])
    
    if y-1>-1:
        if not visited[x][y-1]:
            visited[x][y-1] = True
            sharkMove(x, y-1, cnt+sum(new_fish[x][y-1].values()), lst+[2])
            visited[x][y-1] = False
        else:
            sharkMove(x, y-1, cnt, lst+[2])

    if x+1<=3:
        if not visited[x+1][y]:
            visited[x+1][y] = True
            sharkMove(x+1, y, cnt+sum(new_fish[x+1][y].values()), lst+[3])
            visited[x+1][y] = False
        else:
            sharkMove(x+1, y, cnt, lst+[3])

    if y+1<=3:
        if not visited[x][y+1]:
            visited[x][y+1] = True
            sharkMove(x, y+1, cnt+sum(new_fish[x][y+1].values()), lst+[4])
            visited[x][y+1] = False
        else:
            sharkMove(x, y+1, cnt, lst+[4])

# 냄새 제거
def removeSmell():
    new_smell = {}
    for key in smell:
        if smell[key]>1:
            new_smell[key] = smell[key] - 1
    return new_smell
            
# 1에서 마법사 상어가 뿌린 복제
def copy(fish, new_fish):
    for i in range(4):
        for j in range(4):
            for d, c in fish[i][j].items():
                new_fish[i][j][d] = new_fish[i][j].get(d, 0) + c
    return new_fish

fish, smell = [[dict() for _ in range(4)] for _ in range(4)], {}

M, S = map(int, input().split())
for _ in range(M):
    fx, fy, d = map(int, input().split())
    fish[fx-1][fy-1][d-1] = fish[fx-1][fy-1].get(d-1, 0) + 1
sx, sy = map(int, input().split())
sx -= 1; sy -= 1
dx, dy = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)
sdx, sdy = (0, -1, 0, 1, 0), (0, 0, -1, 0, 1)

while S:
    S -= 1
    # 1. 모든 물고기가 한 칸 이동한다
    new_fish = [[dict() for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d, c in fish[i][j].items():
                nx, ny, d = fishMove(i, j, d)
                new_fish[nx][ny][d] = new_fish[nx][ny].get(d, 0) + c

    # 2. 상어가 연속해서 3칸 이동한다
    visited, ans = [[False] * 4 for _ in range(4)], (0, [5, 5, 5])
    sharkMove(sx, sy, 0, [])

    # 상어가 갈 수 있는 곳으로 위치 이동하고 물고기 격자에서 제거
    for _d in ans[1]:
        sx, sy = sx+sdx[_d], sy+sdy[_d]
        if new_fish[sx][sy] != dict():
            new_fish[sx][sy] = dict()
            smell[(sx, sy)] = 3

    # 3. 격자에서 냄새 제거
    smell = removeSmell()

    fish = copy(fish, new_fish)
ans = sum([sum(r.values()) for row in fish for r in row])
print(ans)
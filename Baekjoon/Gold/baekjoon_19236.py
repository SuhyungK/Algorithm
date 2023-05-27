def copy_dict(dic):
    new_dict = {}
    for k, v in dic.items():
        new_dict[k] = v

    return new_dict

# 청소년 상어
"""
1. 상어가 물고기를 먹는다
2. 물고기가 움직인다
    - 작은 것부터 움직인다
3. 물고기가 다 움직이고 나면 상어가 움직일 수 있는 방향으로 움직인다. 
    - 상어는 물고기가 있는 방향으로만 움직일 수 있다
4. 상어가 움직일 수 있는 곳이 하나도 없다면 = 상어가 갈 수 있는 방향에 물고기가 한 마리도 없다면 상어는 집으로 돌아간다

"""
def move(fish, dir, loc):
    # print(loc)
    for n in range(1, 17):
        if not loc.get(n):
            continue
        x, y = loc[n]
        d = dir[x][y]

        while 1:
            nx, ny = x+dx[d], y+dy[d]
            if nx<0 or ny<0 or nx>3 or ny>3 or fish[nx][ny] == -1:
                d = (d+1)%8
                continue

            if (_n:=fish[nx][ny])>0:
                loc[n], loc[_n] = loc[_n], loc[n]
            else:
                loc[n] = [nx, ny]

            dir[x][y] = d # 물고기가 갖고 있는 방향 업데이트
            fish[nx][ny], fish[x][y] = fish[x][y], fish[nx][ny]
            dir[nx][ny], dir[x][y] = dir[x][y], dir[nx][ny]

            break
        print(n)
        for row in fish:
            print(row)
        print()


def eat(sx, sy, total_eat, fish, dir, loc): # 현재 상어의 위치
    global ans
    
    fish[sx][sy] = -1
    d = dir[sx][sy]

    print('move 전')
    for row in fish:
        print(row)

    # 물고기 움직이기
    move(fish, dir, loc)

    print('move 후', d)
    for row in fish:
        print(row)

    fish[sx][sy] = 0
    cnt = 0
    while 1:
        nx, ny = sx+dx[d], sy+dy[d]
        # 더 이상 갈 수 있는 데가 없음
        if nx<0 or ny<0 or nx>3 or ny>3:
            break
            
        if fish[nx][ny] == 0:
            # 물고기가 없으면 그냥 못 감
            sx, sy = nx, ny
            continue

        # 상어가 잡아먹게 될 물고기의 번호
        f = fish[nx][ny]
        # 상어가 먹어서 물고기의 위치 딕셔너리에는 없어져야 하기 때문에 삭제
        tmp_loc = copy_dict(loc)
        del loc[f]

        # 현재의 물고기 배열 상태를 카피 해둔 다음에 이동 -> 이동하게 되면 물고기가 이동하는 move() 함수가 작동
        tmp_fish = [row[:] for row in fish]
        tmp_dir = [row[:] for row in dir]

        eat(nx, ny, total_eat+f, tmp_fish, tmp_dir, loc)

        # 물고기의 위치와 방향담은 배열도 원상복귀
        # fish = [row[:] for row in tmp_fish]
        # dir = [row[:] for row in tmp_dir]

        # 물고기의 위치 원상복귀
        loc = copy_dict(tmp_loc)
        fish[nx][ny] = f
        
        # 갈 수 있는 곳이 있었기 때문에 cnt += 1
        cnt += 1
        sx, sy = nx, ny

    if not cnt:
        # 먹을 수 있는 물고기가 하나도 없었거나... 이동할 수 있는 방향이 하나도 없었다면 값 비교
        ans = max(ans, total_eat) 
        return 

# 입력받기
dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)
loc = {} # 물고기의 번호에 따른 배열의 위치
fish = [[0]*4 for _ in range(4)] # 물고기의 번호가 담긴 배열
dir = [[0]*4 for _ in range(4)] # 물고기의 이동방향이 담긴 배열
ans = 0
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        n, d = row[2*j:2*j+2]
        loc[n] = [i, j]
        fish[i][j], dir[i][j] = n, d-1

del loc[fish[0][0]]
# for row in fish:
#     print(row)

# for row in dir:
#     print(row)
eat(0, 0, fish[0][0], fish, dir, loc)
print(ans)

# 온풍기 안녕!

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 1. 온풍기에서 바람이 한 번 나옴
def wind(x, y, d):
    tmp = [[0] * C for _ in range(R)]
    tmp[x][y] = 5
    queue = [(x, y)]
    while queue:
        hx, hy = queue.pop(0)
        
        temp = tmp[hx][hy]
        if temp == 1:
            continue    

        if not WALL[d][hx][hy]:
            nx = hx + direction[d][0]
            ny = hy + direction[d][1]
            if -1 < nx < R and -1 < ny < C and not tmp[nx][ny]:
                tmp[nx][ny] = temp - 1
                queue.append((nx, ny))
        
        if d == 0 or d == 1:
            ny = hy + direction[d][1]
            if hx > 0 and -1 < ny < C and not WALL[2][hx][hy] and not WALL[d][hx-1][hy] and not tmp[hx-1][ny]:
                queue.append((hx-1, ny))
                tmp[hx-1][ny] = temp - 1
            
            if hx < R-1 and -1 < ny < C and not WALL[3][hx][hy] and not WALL[d][hx+1][hy] and not tmp[hx+1][ny]:
                queue.append((hx+1, ny))
                tmp[hx+1][ny] = temp - 1
        else:
            nx = hx + direction[d][0]
            if hy > 0 and -1 < nx < R and not WALL[1][hx][hy] and not WALL[d][hx][hy-1] and not tmp[nx][hy-1]:
                queue.append((nx, hy-1))
                tmp[nx][hy-1] = temp - 1
            if hy < C - 1 and -1 < nx < R and not WALL[0][hx][hy] and not WALL[d][hx][hy+1] and not tmp[nx][hy+1]:
                queue.append((nx, hy+1))
                tmp[nx][hy+1] = temp - 1
    return tmp

def raise_temp(arr, tmp):
    for i in range(R):
        for j in range(C):
            arr[i][j] += tmp[i][j]

# 2. 온도가 조절됨(모든 칸에 대해)
def control_temp(arr):
    tmp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if not WALL[3][i][j]:
                if i < R-1:
                    t = abs(arr[i][j] - arr[i+1][j]) // 4
                    if arr[i][j] > arr[i+1][j]:
                        tmp[i+1][j] += t
                        tmp[i][j] -= t
                    else:
                        tmp[i][j] += t
                        tmp[i+1][j] -= t
            if not WALL[0][i][j]:
                if j < C-1:
                    t = abs(arr[i][j] - arr[i][j+1]) // 4
                    if arr[i][j] > arr[i][j+1]:
                        tmp[i][j+1] += t
                        tmp[i][j] -= t
                    else:
                        tmp[i][j] += t
                        tmp[i][j+1] -= t
    return tmp
                    

# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
def decline(arr):
    for i in range(R):
        arr[i][0] = max(0, arr[i][0] - 1)
        arr[i][C-1] = max(0, arr[i][C-1] - 1)
    for j in range(1, C-1):
        arr[0][j] = max(0, arr[0][j] - 1)
        arr[R-1][j] = max(0, arr[R-1][j] - 1)

# 5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사(조사해야 하는 칸 미리 저장)
# 모든 칸의 온도가 K 이상이면 테스트 중단, 
# 도중에 K 미만인 칸이 하나라도 있으면 True 반환해서 게임 계속 진행
def is_finish():
    for x, y in INVEST_ROOM:
        if room_temp[x][y] < K:
            return False
    return True


R, C, K = map(int, input().split())
ROOM = [list(map(int, input().split())) for _ in range(R)]
WALL = [[[False] * C for _ in range(R)] for _ in range(4)]
room_temp = [[0] * C for _ in range(R)]
choco = 0
INVEST_ROOM = []
HEATERS = []

# 각 위치 기준으로 벽에 대한 정보 저장
W = int(input())
for _ in range(W):
    x, y, t = map(int, input().split())
    if t == 0: # 벽이 (x-1, y-1)의 위쪽에 존재
        WALL[2][x-1][y-1] = True
        WALL[3][x-2][y-1] = True
    elif t == 1:
        WALL[0][x-1][y-1] = True
        WALL[1][x-1][y] = True

# 온풍기 위치 찾기 -> 저장
for i in range(R):
    for j in range(C):
        d = ROOM[i][j]
        if d == 5: 
            INVEST_ROOM.append((i, j))
        elif d > 0:
            ni = i + direction[d-1][0]
            nj = j + direction[d-1][1]
            HEATERS.append((ni, nj, ROOM[i][j]-1))

while True:
    for heater in HEATERS:
        raise_temp(room_temp, wind(*heater))
    
    raise_temp(room_temp, control_temp(room_temp))
    decline(room_temp)
    # 4. 초콜릿을 하나 먹는다.
    choco += 1

    if is_finish() or choco > 100:
        break

for i in range(R):
    for j in range(C):
        print(f"{room_temp[i][j]:>3d}", end=" ")
    print()
print(choco)
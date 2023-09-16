# Gaaaaaaaaaarden

# 배양액을 뿌릴 수 있는 땅 찾기
def find_land(arr):
    queue = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                queue.append((i, j))
    return queue

# 배양액을 뿌릴 수 있는 중복조합 구하기
def dfs(i, k, tmp, lst, comb):
    if len(tmp) == k:
        comb.append(tmp[:])
        return comb
    
    for j in range(i, len(lst)):
        if lst[j] not in tmp:
            tmp.append(lst[j])
            comb = dfs(j+1, k, tmp, lst, [row[:] for row in comb])
            tmp.remove(lst[j])
    return comb

# 배양액 퍼뜨리기
def bfs(green, red, medium_land):
    arr = [[[0, 0] for _ in range(m)] for _ in range(n)]
    queue = []
    for i in green:
        gx, gy = medium_land[i]
        arr[gx][gy] = [GREEN, 0]
        queue.append((gx, gy))
    for j in red:
        rx, ry = medium_land[j]
        arr[rx][ry] = [RED, 0]
        queue.append((rx, ry))

    flowers = 0
    while queue:
        x, y = queue.pop(0)

        # 현재 탐색하려는 칸이 이미 꽃이라면 탐색 불가
        if arr[x][y][0] == FLOWER:
            continue
        count = arr[x][y][1]
        for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            # 범위에 속하지 않거나 호수이거나 같은 색의 배양액이거나 꽃인 경우
            if not(-1<nx<n and -1<ny<m) or land[nx][ny] == 0 or arr[nx][ny][0] in (arr[x][y][0], 3):
                continue
                
            if arr[x][y][0] == GREEN:
                if arr[nx][ny][0] == RED and arr[nx][ny][1] == count+1:
                    arr[nx][ny][0] = FLOWER
                    flowers += 1
            elif arr[x][y][0] == RED:
                if arr[nx][ny][0] == GREEN and arr[nx][ny][1] == count+1:
                    arr[nx][ny][0] = FLOWER
                    flowers += 1
            if arr[nx][ny][0] == EMPTY:
                arr[nx][ny] = [arr[x][y][0], count+1]
                queue.append((nx, ny))

    return flowers

n, m, g, r = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

medium_land = find_land(land)
combs, lst, max_result = [], range(len(medium_land)), 0
EMPTY, GREEN, RED, FLOWER = 0, 1, 2, 3
for green in dfs(0, g, [], lst, []):
    for red in dfs(0, r, [], [row for row in lst if row not in green], []):
        max_result = max(max_result, bfs(green, red, medium_land))

print(max_result)
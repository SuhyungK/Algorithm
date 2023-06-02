# 주사위 굴리기 2

# 점수 획득
def bfs(x, y, B):
    q = [(x, y)]
    idx = 0
    while idx<len(q):
        x, y = q[idx]

        idx += 1
        # 동서남북 방향으로 연속해서 이동할 수 있는지
        for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):

            # 이동할 수 있는 칸의 값은 모두 B여야 하고 방문한 적이 없어야 함
            if -1<ny<M and -1<nx<N and MAP[nx][ny] == B and (nx, ny) not in q:
                q.append((nx, ny))
    
    for _x, _y in q:
        MAP[_x][_y] = (B, len(q))

def move(A, B, d):
    if A > B:
        return (d+1)%4
    elif A < B:
        return (d+3)%4
    return d

def tumble(D, a, b, c, d, e, f):
    if D == 0:
        return d, b, a, f, e, c
    elif D == 1:
        return b, f, c, d, a, e
    elif D == 2:
        return c, b, f, a, e, d
    elif D == 3:
        return e, a, c, d, f, b

def sol():
    global K
    dice = [d for d in range(1, 7)]
    x = y = d = ans = 0
    
    while K:
        # 1. 주사위가 이동 방향으로 한 칸 굴러간다
        nx, ny = x+dx[d], y+dy[d]

        # 만약, 이동 방향에 칸이 없다면 이동 방향을 반대로 한 다음에 한 칸 굴러간다
        if ny<0 or nx<0 or ny>=M or nx>=N:
            d = (d+2)%4
            nx, ny = x+dx[d], y+dy[d]

        dice = list(tumble(d, *dice))
        # print(dice)
        x, y = nx, ny

        # 2. 주사위가 도착한 칸에 대한 점수를 획득한다
        B, C = MAP[x][y]
        ans += B*C

        # 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸의 값을 비교해서 이동방향 결정
        d = move(dice[-1], B, d)

        # 주사위 이동 횟수 차감
        K -= 1

    return ans

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
visit = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if type(B:=MAP[i][j]) == int:
            bfs(i, j, B)

print(sol())
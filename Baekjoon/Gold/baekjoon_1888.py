from collections import defaultdict

N, M = map(int, input().split())
wall = [list(map(int, input())) for _ in range(N)]
total = N * M
mold = defaultdict(list)

#-------------------함수 정의 시작--------------
def bfs(_i, _j):
    global mold
    q = [(_i, _j)]
    cnt = 1
    while q:
        _r, _c = q.pop(0)
        for _dr, _dc in (-1, 0), (1, 0), (0, 1), (0, -1):
            nr, nc = _r + _dr, _c + _dc
            if -1 < nr < N and -1 < nc < M and wall[nr][nc]:
                if visit[nr][nc] < day:
                    visit[nr][nc] = day
                    q.append((nr, nc))
                    cnt += 1
    # bfs 돌려서 한 번에 세서 나온 곰팡이의 개수가 (전체 개수 - 0의 개수)랑 같으면 곰팡이가 한 덩어리가 된 거
    return cnt == total - sum(wall, []).count(0)

# 덩어리인가??
def isLump():
    global mold
    for i in range(N):
        for j in range(M):
            if wall[i][j] and visit[i][j] != day:
                visit[i][j] = day
                # isLump()는 한 번만 실행되면 되고 bfs가 True면 바로 while문 종료
                # bfs가 False면 곰팡이 퍼뜨리고 다시 실행
                return bfs(i, j)

#--------------------함수 정의 끝--------------

day = 0
visit = [[-1] * M for _ in range(N)]

# mold = { 속도 : [그 속도를 가지는 좌표값] }
for i in range(N):
    for j in range(M):
        if wall[i][j]:
            mold[wall[i][j]].append((i, j))

# 덩어리가 아닐때만 무한반복 / 덩어리가 되면 while 문 종료
while not isLump():

    mold = dict(sorted(mold.items(), reverse=1))

    for v, q in mold.items():
        new_q = []
        while q:
            r, c = q.pop(0)
            # 곰팡이가 퍼질 수 있는 범위가 좌표 범위를 벗어나지 않게 range 설정
            for nr in range(0 if (-1)*v+r <= 0 else (-1)*v+r, N if v+r >= N else v+r+1):
                for nc in range(0 if (-1)*v+c <= 0 else (-1)*v+c, M if v+c >= M else v+c+1):
                    if wall[nr][nc] < v:
                        wall[nr][nc] = v
                        new_q.append((nr, nc))
        # v의 속도를 가지는 좌표값들을 새로 구했기 때문에 mold 값 변경
        mold[v] = new_q[:]
    day += 1

print(day)
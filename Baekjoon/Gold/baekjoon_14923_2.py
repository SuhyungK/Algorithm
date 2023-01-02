# BOJ Gold 4 미로 탈출
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Hx, Hy = map(lambda x: int(x) - 1, input().split())
Ex, Ey = map(lambda x: int(x) - 1, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    v = [[0] * M for _ in range(N)]
    q = [(Hx, Hy, False)]
    next_q = []
    turn = 0
    v[Hx][Hy] = 1
    while q:
        while q:
            r, c, wall_broken = q.pop(0)
            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                
                if (nr, nc) == (Ex, Ey):
                    return turn + 1

                # 벽인 경우 : 벽이 아직 부서지지 않고 이곳을 방문한 적이 한 번도 없어야 함
                if arr[nr][nc] == 1:
                    if wall_broken == False and v[nr][nc] == 0:
                        v[nr][nc] = 2
                        next_q.append((nr, nc, True))

                # 벽이 아닌 경우
                else:
                    # 1. 벽이 아직 한 번도 부서지지 않았고 벽이 부서지지 않은 상태에서는 이곳을 방문한 적이 없어야 함
                    if wall_broken == False and v[nr][nc] != 1:
                        v[nr][nc] = 1
                        next_q.append((nr, nc, wall_broken))
                    # 2. 벽이 한 번 부서졌고 벽이 한 번 부서진 상태에서는 이곳을 방문한 적이 없음
                    # (벽이 부서지지 않은 상태에서는 한 번 방문한 적이 있어도 됨)
                    elif wall_broken == True and v[nr][nc] != 2:
                        v[nr][nc] = 2
                        next_q.append((nr, nc, wall_broken))
                # print()
                # for row in v:
                #     print(row)
                # print()

        if next_q:
            q = next_q[:]
            turn += 1
    return -1

print(bfs())
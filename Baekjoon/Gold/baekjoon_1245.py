# BOJ 농장 관리

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
dr = [1, -1, 1, -1, 1, -1, 0, 0]
dc = [0, 0, 1, 1, -1, -1, 1, -1]
cnt = 0

for i in range(N):
    for j in range(M):
        if v[i][j] == 0: # 아직 방문하지 않은 곳이면
            st = [(i, j)]
            isPeak = True
            v[i][j] = 1
            while st:
                r, c = st.pop()
                for k in range(8):
                    nr, nc = r + dr[k], c + dc[k]
                    if -1 < nr < N and -1 < nc < M:
                        # 아직 방문하지 않은 곳이고 탐색하고 있는 곳의 높이와 같다면
                        if v[nr][nc] == 0 and arr[nr][nc] == arr[i][j]:
                            st.append((nr, nc))
                            v[nr][nc] = 1

                        # 더 높은 곳이 있다면.... 
                        elif arr[nr][nc] > arr[r][c]:
                            isPeak = False

            if isPeak:
                print((i, j))
                cnt += 1

print(cnt)
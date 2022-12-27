# BOJ 2583 영역 구하기
M, N, K = map(int, input().split())
crd = [list(map(int, input().split())) for _ in range(K)]
area = [[0] * N for _ in range(M)]

for row in crd:
    x1, y1, x2, y2 = row
    for y in range(y1, y2):
        for x in range(x1, x2):
            area[y][x] = 1

res = []
for i in range(M):
    for j in range(N):
        if not area[i][j]:
            area[i][j] = 1
            st = [(i, j)]
            cnt = 1
            while st:
                r, c = st.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if -1 < nr < M and -1 < nc < N and not area[nr][nc]:
                        area[nr][nc] = 1
                        st.append((nr, nc))
                        cnt += 1
            res.append(cnt)

print(len(res))
print(*sorted(res))
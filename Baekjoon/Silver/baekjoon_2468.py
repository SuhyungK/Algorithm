# 안전 영역

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

temp = []
for i in range(N):
    temp.extend(arr[i])

res = 1
for t in range(min(temp), max(temp)):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > t and v[i][j] != t:
                cnt += 1
                q = [(i, j)]
                v[i][j] = t
                while q:
                    r, c = q.pop(0)
                    for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
                        nr, nc = dr + r, dc + c
                        if -1 < nr < N and -1 < nc < N and arr[nr][nc] > t and v[nr][nc] != t:
                            v[nr][nc] = t
                            q.append((nr, nc))
    res = max(res, cnt)

print(res)
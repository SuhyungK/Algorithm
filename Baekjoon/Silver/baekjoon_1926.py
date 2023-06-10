# 그림

n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]

def find_paint(si, sj):
    q = [(si, sj)]
    cnt = 1
    while q:
        i, j = q.pop(0)
        for ni, nj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if ni<0 or ni>=n or nj<0 or nj>=m or paint[ni][nj] == 0:
                continue
            cnt += 1
            paint[ni][nj] = 0
            q.append((ni, nj))

    return cnt

size = cnt = 0
for i in range(n):
    for j in range(m):
        if paint[i][j]:
            paint[i][j] = 0
            cnt += 1
            size = max(size, find_paint(i, j))

print(cnt)
print(size)
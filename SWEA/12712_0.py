# 파리퇴치3

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0

    for i in range(n):
        for j in range(n):
            sum1 = sum2 = arr[i][j]
            for d in range(1,m):
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni, nj = i + di * d, j + dj * d
                    if 0 <= ni < n and 0 <= nj < n:
                        sum1 += arr[ni][nj]

                for dx, dy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                    nx, ny = i + dx * d, j + dy * d
                    if 0 <= nx < n and 0 <= ny < n:
                        sum2 += arr[nx][ny]

            cnt = max(sum1, sum2)
            if maxV < cnt:
                maxV = cnt
    print(f'#{tc}', maxV)
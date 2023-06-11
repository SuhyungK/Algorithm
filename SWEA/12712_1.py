# 파리퇴치3

def fly(cur, i, j, d):
    global sumV
    ni = i + d[0]
    nj = j + d[1]

    if cur == m-1 or ni < 0 or ni >= n or nj < 0 or nj >= n:
        return
    sumV += arr[ni][nj]
    fly(cur+1, ni, nj, d)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0

    D = [[(0, 1), (1, 0), (-1, 0), (0, -1)], [(-1, -1), (-1, 1), (1, -1), (1, 1)]]
    for i in range(n):
        for j in range(n):
            for delta in D:
                sumV = arr[i][j]
                for d in delta:
                    fly(0, i, j, d)
                maxV = max(maxV, sumV)

    print(f'#{tc}', maxV)
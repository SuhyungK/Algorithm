import math

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    n = (N - 1) // 2
    mid = N // 2
    res = 0
    for i in range(N):
        for j in range(N):
            if math.sqrt((mid - i) ** 2 + (mid - j) ** 2) <= 2:
                res += arr[i][j]

    print(f'#{tc}', res)
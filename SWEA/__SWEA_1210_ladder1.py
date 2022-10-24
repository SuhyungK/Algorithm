from re import L


T = int(input())
for tc in range(1, T+1):
    N, M, K= map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    for _ in range(M):
        y, x, n, d = map(int, input().split()) # 세로, 가로, 미생물 수, 이동방향
        arr[y][x] = (n, d)

    print(f'#{tc}')
    for row in arr:
        print(*row)
        
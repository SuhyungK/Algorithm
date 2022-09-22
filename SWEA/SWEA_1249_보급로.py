T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    queue = [(0, 0, 0)]

    while queue:
        i, j, s = queue.pop(0)
        for di, dj in ((0, 1), (1, 0)):
            ni, nj = i+di, j+dj
            if -1 < ni < N and -1 < nj < N:
                queue.append((ni, nj, s+arr[ni][nj]))

        if (i, j) == (N-1, N-1):
            print(queue)

    print(f'#{tc}')
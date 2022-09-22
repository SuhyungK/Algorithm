def queen(i):
    global cnt
    if i == N:
        cnt += 1
        return

    for j in range(N):
        if visit[j] == 0:
            for k in range(1, i+1):
                if i-k >= 0 and j-k >= 0 and arr[i-k][j-k]:
                    break
                if i-k >= 0 and j+k < N and arr[i-k][j+k]:
                    break
            else:
                visit[j] = 1
                arr[i][j] = 1
                queen(i+1)
                arr[i][j] = 0
                visit[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visit = [0] * N
    cnt = 0

    queen(0)
    print(f'#{tc}', cnt)
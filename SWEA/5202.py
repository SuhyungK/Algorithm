# 화물도크

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key=lambda x:(x[1], x[0]))

    maxV = i = 0
    while i < N-1:
        cnt, j = 0, i+1
        while j < N:
            if time[i][1] <= time[j][0]:
                cnt += 1
                i = j
            j += 1
        if maxV < cnt:
            maxV = cnt +1
        i += 1

    print(f'#{tc}', maxV)
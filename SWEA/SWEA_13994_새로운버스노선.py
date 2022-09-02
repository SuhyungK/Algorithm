T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stop = [0] * 1001

    for _ in range(N):
        t, a, b = map(int, input().split())
        stop[a] += 1
        stop[b] += 1
        if t == 1:
            for i in range(a+1, b):
                stop[i] += 1
        elif t == 2:
            for j in range(a+2, b, 2):
                stop[j] += 1
        else:
            if a % 2:
                for k in range(a+1, b):
                    if not k % 3 and k % 10:
                        stop[k] += 1
            else:
                for k in range(a+1, b+1):
                    if not k % 4:
                        stop[k] += 1
    print(f'#{tc}',max(stop))
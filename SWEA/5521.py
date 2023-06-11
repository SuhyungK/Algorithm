# 상원이의 생일파티

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    visit = [0] * (N+1)
    cnt = 0
 
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    stack = [(1, 1)]
    visit[1] = 1
    while stack:
        s, c = stack.pop()
        if c >= 3:
            continue
        for i in arr[s]:
            if visit[i] == 0:
                visit[i] = c+1
                cnt += 1
            elif visit[i] > c+1:
                visit[i] = c+1
            stack.append((i, c+1))            

    print(f'#{tc}', cnt)
def dfs(k, n, sumV):
    global minV
    if k == n:
        if minV < sumV:
            minV = sumV
    # 3행에 도달하면 알아서 종료되기 때문에 else 사용할 필요 X
    if minV < sumV:
        return
    # 부분합이 최소합보다 커지면 알아서 종료되기 때문에 else 사용 X
    for i in range(n):
        if not temp[i]:
            temp[i] = True
            dfs(k+1, n, sumV+arr[k][i])
            temp[i] = False

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    minV = 10 * n
    temp = [False] * n

    dfs(0, n, 0)
    print(f'#{tc}', minV)
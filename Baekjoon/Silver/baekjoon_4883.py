# 삼각 그래프

tc = 1
MAX_INT = 1e9

while True:
    n = int(input())
    if not n:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = MAX_INT, graph[0][1], graph[0][1]+graph[0][2]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + graph[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + graph[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1]) + graph[i][2]

    print(f'{tc}. {dp[-1][1]}')
    tc += 1
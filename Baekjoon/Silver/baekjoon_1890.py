# 점프

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        x = board[i][j]
        if x:
            if j+x<N:
                dp[i][j+x] += dp[i][j]
            if i+x<N:
                dp[i+x][j] += dp[i][j]


print(dp[-1][-1])
# 가장 큰 정사각형

n, m = map(int, input().split())
square = [list(map(int, input())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0] = square[0]
for i in range(n):
    dp[i][0] = square[i][0]

for i in range(1, n):
    for j in range(1, m):
        if square[i][j]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

ans = 0
for row in dp:
    ans = max(ans, max(row))
print(ans**2)
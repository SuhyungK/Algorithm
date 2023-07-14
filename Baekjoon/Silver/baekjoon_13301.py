# 타일 장식물

n = int(input())
dp = [[0, 0] for _ in range(n+2)]
dp[0] = [1, 1]
dp[1] = [1, 0]

for i in range(1, n, 2):
    dp[i][1] = dp[i+1][1] = dp[i-1][0]+dp[i-1][1]
    dp[i+1][0] = dp[i+2][0] = dp[i][0]+dp[i][1]

print(sum(dp[n-1])*2)
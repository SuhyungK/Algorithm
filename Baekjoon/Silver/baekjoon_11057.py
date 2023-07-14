# 오르막 수

n = int(input())
dp = [1]*10

for i in range(1, n+1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(dp[9]%10007)
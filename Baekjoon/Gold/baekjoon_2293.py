# 동전 1

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]*(k+1)

for i in range(n):
    coin = coins[i]
    if coin > k:
        continue
    dp[coin] += 1
    for j in range(coin+1, k+1):
        dp[j] += dp[j-coin]

print(dp[k])
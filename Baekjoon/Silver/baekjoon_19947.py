# 투자의 귀재 배주형

H, Y = map(int, input().split())

dp = [0]*(Y+5)
dp[4] = H

for i in range(5, Y+5):
    dp[i] = max(int(dp[i-1]*1.05), int(dp[i-3]*1.2), int(dp[i-5]*1.35))
print(dp[-1])
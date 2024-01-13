# 돌 게임 3

dp = [0]*1001
dp[1], dp[2], dp[3], dp[4] = 1, 2, 1, 1

N = int(input())
for i in range(5, N+1):
    dp[i] = min(dp[i-1], dp[i-3], dp[i-4])+1

print(dp[:10])
if dp[N]%2:
    print("SK")
else:
    print("CY")
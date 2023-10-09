# 극장 좌석

dp = [0 for _ in range(41)]
dp[0], dp[1] = 1, 1
for i in range(2, 41):
    dp[i] = dp[i-1]+dp[i-2]

N = int(input())
M = int(input())

ans, t = 1, 0
for _ in range(M):
    x = int(input())
    ans *= dp[x-t-1]
    t = x
ans *= dp[N-t]
print(ans)
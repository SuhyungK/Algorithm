# 퇴사 

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    t, p = lst[i]
    if t+i <= N:
        dp[i] = max(dp[t+i] + p, dp[i+1]) 
    else:
        dp[i] = dp[i+1]

print(dp[0])
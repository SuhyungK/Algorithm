# 가장긴증가하는부분수열

N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))

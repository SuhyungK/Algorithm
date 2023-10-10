# 자두나무

T, W = map(int, input().split())
nums = [int(input()) for _ in range(T)]

rem = 1
dp = [[0]*(T+1) for _ in range(W+1)]
for i in range(1, T+1):
    if nums[i-1]%2 == rem:
        dp[0][i] = dp[0][i-1]+1
    else:
        dp[0][i] = dp[0][i-1]

for i in range(1, W+1):
    rem = (rem+1)%2
    for j in range(i, T+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])
        if nums[j-1]%2 == rem:
            dp[i][j] += 1

print(max(list(map(list, zip(*dp)))[-1]))
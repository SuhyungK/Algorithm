# 이친수

def sol(N):
    if N == 1:
        return 1
    
    dp = [[0, 0] for _ in range(N-1)]
    dp[0] = [1, 0]
    for i in range(1, N-1):
        dp[i][0] = sum(dp[i-1])
        dp[i][1] = dp[i-1][0]
    
    return sum(dp[-1])

N = int(input())
print(sol(N))
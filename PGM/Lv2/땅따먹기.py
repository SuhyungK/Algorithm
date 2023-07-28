def solution(land):
    N = len(land)
    dp = [[0, 0, 0, 0] for _ in range(N)]
    dp[0] = land[0]
    
    for i in range(1, N):
        dp[i][0] = land[i][0] + max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        dp[i][1] = land[i][1] + max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
        dp[i][2] = land[i][2] + max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
        dp[i][3] = land[i][3] + max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        
    return max(dp[N-1])
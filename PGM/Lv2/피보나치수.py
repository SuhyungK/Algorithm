def solution(n):
    dp = [0] * (n+1) 
    dp[1] = 1

    idx = 2
    while idx <= n:
        dp[idx] = (dp[idx-1] + dp[idx-2])%1234567
        idx += 1

    return dp[n]
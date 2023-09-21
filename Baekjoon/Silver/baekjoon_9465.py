# 스티커

def sol(n, dp):
    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        
        if n > 2:
            for i in range(2, n):
                dp[0][i] += max(dp[1][i-1], dp[1][i-2])
                dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
    for row in dp:
        print(row)
    return max(dp[0][-1], dp[1][-1])
    
for _ in range(int(input())):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    print(sol(n, dp))
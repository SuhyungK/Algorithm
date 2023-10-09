# 2xn 타일링 2

def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 3
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]*2
    return dp[-1]

print(sol(int(input()))%10007)
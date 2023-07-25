# 피자(Small)

N = int(input())

def solution():
    if N == 1:
        return 0
    
    if N == 2:
        return 1
    
    dp = [0] * (N+1)
    dp[2] = 1
    
    for i in range(3, N+1):
        a, b = i//2, i-i//2
        dp[i] = dp[a] + dp[b] + a*b
    
    print(dp)
    return dp[-1]

print(solution())

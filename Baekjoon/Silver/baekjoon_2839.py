# 설탕 배달 

N = int(input())

def solution():
    if N == 3 or N == 5:
        return 1
    
    if N == 4:
        return -1
    
    dp = [1e9]*(N+1)
    dp[3] = dp[5] = 1
    for i in range(6, N+1):
        dp[i] = min(dp[i-3], dp[i-5])+1

    if dp[N] >= 1e9:
        return -1
    return dp[-1]

print(solution())
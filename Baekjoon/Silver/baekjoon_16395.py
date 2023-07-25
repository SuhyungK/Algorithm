# 파스칼의 삼각형

def sol(n, k):
    if n == 1 or n == 2:
        return 1
    
    dp = [1, 1]
    i = 2
    while i < n:
        new_dp = [1]
        for j in range(len(dp)-1):
            new_dp.append(dp[j]+dp[j+1])
        new_dp.append(1)
        i += 1
        dp = new_dp[:]
    
    return dp[k-1]

n, k = map(int, input().split())

print(sol(n, k))
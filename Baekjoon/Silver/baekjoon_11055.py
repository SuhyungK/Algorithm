# 가장 큰 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))
dp = [A[i] for i in range(N)]

print(dp)
for i in range(N):
    for j in range(i+1, N):
        if A[i]<A[j] and dp[j]<dp[i]+A[j]:
            dp[j] = dp[i]+A[j]

print(max(dp))
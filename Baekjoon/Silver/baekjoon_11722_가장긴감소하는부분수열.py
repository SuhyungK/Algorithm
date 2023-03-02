# N = int(input())
# lst = list(map(int, input().split()))
# dp = [1] * N

# for i in range(N):
#     for j in range(i):
#         if lst[j] < lst[i] and dp[i] < dp[j] + 1:
#             dp[i] = dp[j] + 1

# print(max(dp))



























N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N 

for i in range(N):
    k = dp[i]
    for j in range(i+1, N):
        if arr[j] < arr[i] and dp[j] < dp[i] + 1:
            dp[j] = k + 1

print(max(dp))
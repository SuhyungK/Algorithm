# 수열

N = int(input())
arr = list(map(int, input().split()))
dp_i, dp_d = [1] * N, [1] * N

for i in range(1, N):
    if arr[i-1] <= arr[i]:
       dp_i[i] += dp_i[i-1]
    if arr[i-1] >= arr[i]:
        dp_d[i] += dp_d[i-1]
 
print(max(max(dp_i), max(dp_d)))
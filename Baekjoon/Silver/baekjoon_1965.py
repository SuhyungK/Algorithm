# 상자넣기

N = int(input())
box = list(map(int, input().split()))
dp = [1] * N

for i in range(N-1):
    b, t = box[i], dp[i]
    for j in range(i+1, N):
        if b < box[j]:
            dp[j] = max(dp[j], t + 1)
            
print(max(dp))
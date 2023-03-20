# 상자넣기

n = int(input())
box = list(map(int, input().split()))
dp = [1] * n

for i in range(n-1):
    b, t = box[i], dp[i]
    for j in range(i+1, n):
        if b < box[j]:
            dp[j] = max(dp[j], t + 1)
            
print(max(dp))
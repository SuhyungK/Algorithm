# BOJ 카드 구매하기

N = int(input())
card = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = card[0]

for i in range(N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + card[j - 1])

print(dp[N])
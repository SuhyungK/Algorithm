# S1 포도주 시식

# # 1
# n = int(input())
# lst = [int(input()) for _ in range(n)]

# if n == 1:
#     print(lst[0])
# else:
#     dp = [[0, 0, 0] for _ in range(n)]
#     dp[0] = [0, lst[0], 0]
#     dp[1] = [lst[0], lst[1], lst[0]+lst[1]]

#     for i in range(2, n):
#         dp[i][0] = max(dp[i-1]) # 그 포도주를 마시지 않았을 때
#         dp[i][1] = max(max(dp[i-2]), dp[i-1][0])+lst[i] # 그 포도주를 마셨을 때 (1잔 연속)
#         dp[i][2] = dp[i-1][1]+lst[i] # 그 포도주를 마셨을 때 (2잔 연속)

#     print(max(dp[n-1]))

# 2
"""
1. 그 잔의 포도주를 아예 안 마셨을 때
2. 1잔 연속 마셨을 때(두 번째 전에 있던 잔을 마신 경우 가능)
3. 2잔 연속 마셨을 때(직전 잔에 있던 포도주를 반드시 마셔야 함)
"""

import sys

n = int(input())
W = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * (n+1)

dp[1] = W[0]

if n > 1:
    dp[2] = W[1] + dp[1]

if n > 2:
    for i in range(3, n+1):
        # dp[i-1] : 안 마셨을 때
        # W[i-1] + dp[i-2] : 현재 잔을 마셨을 때(1잔 연속; 두 번째 전 잔을 마셨을 때 값 가져와서 더하면됨)
        # W[i-1] + W[i-2] + dp[i-3] : 현재 잔을 마셨을 때(2잔 연속; 직전 잔을 "1잔 연속" 마셨을 때 식 + 현재 포도주 잔)
        dp[i] = max(dp[i-1], W[i-1] + dp[i-2], dp[i-3] + W[i-1] + W[i-2])

print(dp[n])

# 3
n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [0] * (n+1)

# n = 1,2 면 걍 다 마시는게 이득
dp[1] = lst[0]

if n > 1:
    dp[2] = lst[0] + lst[1]

# n이 3보다 크면 
# max(그 잔을 안 마셨을 때, 1잔 연속 마셨을 때, 2잔 연속 마셨을 때)
# 값을 dp[i]에 저장
if n > 2:
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + lst[i-1], dp[i-3] + lst[i-1] + lst[i-2])

print(dp[n])
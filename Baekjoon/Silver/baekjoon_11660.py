# 구간 합 구하기 5

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(M)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        arr[i][j] = arr[i][j] + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

for l in lst:
    x1, y1, x2, y2 = l
    print(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])
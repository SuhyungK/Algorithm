# 플로이드

import sys
input = sys.stdin.readline

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1e9:
                arr[i][j] = 0

n = int(input().strip())
m = int(input().strip())
arr = [[1e9] * n for _ in range(n)]

# 자기 자신에게 가는 비용은 0
for i in range(n):
    arr[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().strip().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)

floyd()
for row in arr:
    print(*row)

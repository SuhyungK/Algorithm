# 안테나

import sys
input = sys.stdin.readline

N = int(input())
house = list(map(int, input().split()))
m, M = max(house), sum(house)
lst = [0] * (m + 1)
res = [0] * (m + 1)

for h in house:
    lst[h] += 1

p = 0
for i in range(1, m + 1):
    tmp = lst[i]
    res[i] = res[i-1] + 2 * p - N
    p += tmp

print(res.index(min(res)))
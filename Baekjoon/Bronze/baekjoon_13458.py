# 시험 감독

import math, sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

res = N
for a in A:
  if (t:=a - B) > 0:
    res += math.ceil(t / C)

print(res)
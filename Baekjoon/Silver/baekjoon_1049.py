# 기타줄
"""

"""
import math 

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
lst = list(map(list, zip(*lst)))

a, b = min(lst[0]), min(lst[1])

res = 0
if a // b >= 6:
    res = math.ceil(N/6) * a
else:
    if (N % 6) > a // b:
        res = math.ceil(N/6) * a
    else:
        res = N // 6 * a + (N % 6) * b

print(res)
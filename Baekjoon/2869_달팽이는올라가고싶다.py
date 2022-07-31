# 1
# 시간초과로 반복문 돌리면 실패하는 문제

import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
D = (V - B) / (A - B)

print(int(D) if D == int(D) else int(D)+1)


# 2
import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())
D = (V - B) / (A - B)

print(math.ceil(D))

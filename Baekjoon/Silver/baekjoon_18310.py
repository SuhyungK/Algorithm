# 안테나
"""
처음부터 끝까지 모든 집을 다 돌면서 앞에 있는 집의 개수들만큼은 계속 더해주고
뒤에 있는 집의 개수들만큼은 계속 빼줌
앞에 있는 집들은 뒤로 갈수록 멀어지니까 거리가 증가하고, 뒤에 있는 집들은 뒤로 갈수록 가까워지니까 거리가 감소하므로
"""
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
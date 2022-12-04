# 카드 정렬하기

from heapq import heappush, heappop

N = int(input())
pq = []
for _ in range(N):
    heappush(pq, int(input()))

# 묶음이 하나인 경우는 비교할 게 없음
if N == 1:
    print(0)
    exit()

res = 0
while len(pq)>1:
    x = heappop(pq)
    x += heappop(pq)
    res += x
    heappush(pq, x)

print(res)
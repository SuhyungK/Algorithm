# 행성 연결

from heapq import heappush, heappop

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

pq, MST, cost = [(0, 0)], set(), 0
while pq:
    w, x = heappop(pq)
    if x in MST:
        continue

    MST.add(x)
    cost += w
    for i, _w in enumerate(arr[x]):
        if i in MST:
            continue
        heappush(pq, (_w, i))

print(cost)
import heapq

N = int(input())
heap = []
res = []

for _ in range(N):
    item = int(input())
    if item:
        heapq.heappush(heap, -item)
    else:
        if len(heap) == 0:
            res.append(0)
        else:
            res.append(-heapq.heappop(heap))

for r in res:
    print(r)
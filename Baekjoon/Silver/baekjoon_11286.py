# 절대값 힙

import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x:
        if x > 0:
            heapq.heappush(heap, (x, 1))
        else:
            heapq.heappush(heap, (-x, 0))
    else:
        if len(heap) == 0:
            print(0)
        else:
            y = heapq.heappop(heap)
            print(-y[0]) if y[1] == 0 else print(y[0])

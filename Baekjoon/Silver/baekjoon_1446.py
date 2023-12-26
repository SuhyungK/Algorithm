# 지름길

import heapq
from collections import defaultdict

def dijkstra(start):
    Q = [(0, start)]
    dist = [i for i in range(D+1)]
    while Q:
        w, now = heapq.heappop(Q)

        if now > D or w > dist[now]:
            continue
        dist[now] = w
        for next, next_w in node[now]:
            heapq.heappush(Q, (w + next_w, next))
        heapq.heappush(Q, (w + 1, now + 1))
            
    return dist[-1]

N, D = map(int, input().split())
node = defaultdict(list)

for _ in range(N):
    s, e, d = map(int, input().split())
    node[s].append((e, d))
print(dijkstra(0))

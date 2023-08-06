# 최소비용 구하기

import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
buses = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().strip().split())
    buses[s].append((e, c))

s, e = map(int, input().strip().split())
hq = []

def djikstra(s, e):
    cost = [1e9]*(N+1)
    cost[s] = 0
    heapq.heappush(hq, (0, s))

    while hq:
        now_cost, now = heapq.heappop(hq)
        if now == e:
            return cost[now]
        if now_cost > cost[now]:
            continue
        for x, c in buses[now]:
            if cost[x] <= now_cost + c:
                continue
            cost[x] = now_cost + c
            heapq.heappush(hq, (cost[x], x))

    return cost[e]
    
print(djikstra(s, e))
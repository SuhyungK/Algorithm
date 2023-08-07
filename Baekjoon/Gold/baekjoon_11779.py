# 최소비용 구하기 2

import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
buses = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().strip().split())
    buses[e].append((s, c))

s, e = map(int, input().strip().split())
hq = []

def djikstra(s, e):
    cost = [1e9]*(N+1)
    routes = [-1] * (N+1)
    routes[s] = s
    cost[s] = 0
    heapq.heappush(hq, (0, s))

    while hq:
        now_cost, now = heapq.heappop(hq)
        if now == e:
            result = cost[now]
            route = []
            while now != routes[now]:
                route.append(now)
                now = routes[now]
            return route+[s], result
        if now_cost > cost[now]:
            continue
        for x, c in buses[now]:
            if cost[x] <= now_cost + c:
                continue
            cost[x] = now_cost + c
            routes[x] = now
            heapq.heappush(hq, (cost[x], x))

    return cost[e]
    
answer = djikstra(e, s)
print(answer[1])
print(len(answer[0]))
print(*answer[0])
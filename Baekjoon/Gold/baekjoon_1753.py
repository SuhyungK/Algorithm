# 최단경로

import heapq

V, E = map(int, input().split())
K = int(input())

arr = [dict() for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if not arr[u].get(v): # 두 정점 사이에 간선이 존재하지 않는다면
        arr[u][v] = w
    elif arr[u][v] > w: # 두 정점 사이에 간선이 이미 존재한다면 더 작을 경우에만 저장
        
        arr[u][v] = w

def djikstra():
    cost = [float('inf') for _ in range(V+1)]
    cost[K] = 0
    pq = [(0, K)]

    while pq: 
        c, u = heapq.heappop(pq)
        if cost[u] < c:
            continue

        for v, w in arr[u].items():
            if cost[v] > c+w:
                cost[v] = c+w
                heapq.heappush(pq, (cost[v], v))

    return cost

result = djikstra()[1:]

for r in result:
    if r == float('inf'):
        print('INF')
    else:
        print(r)
# 달빛 여우

from collections import defaultdict
from heapq import heappop, heappush

def move_wolf(n, graph):
    dist = [[1e9, 1e9] for _ in range(n+1)]
    dist[1][0] = 0

    pq = [(0, 1, 0)]
    while pq:
        w, i, v = heappop(pq)
        if dist[i][v] != w:
            continue
        
        if v == 0:
            for j, _w in graph[i]:
                cost = w+_w/2
                if dist[j][1] > cost:
                    heappush(pq, (cost, j, 1))
                    dist[j][1] = cost
        else:
            for j, _w in graph[i]:
                cost = w + _w*2
                if dist[j][0] > cost:
                    heappush(pq, (cost, j, 0))
                    dist[j][0] = cost
    return list(map(min, dist[1:]))

def move_fox(n, graph):
    dist = [1e9]*(n+1)
    dist[1] = 0

    pq = [(0, 1)]
    while pq:
        w, i = heappop(pq)
        if dist[i] != w:
            continue

        for j, _w in graph[i]:
            cost = w+_w
            if dist[j] > cost:
                dist[j] = cost
                heappush(pq, (cost, j))

    return dist[1:]

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])
    graph[b].append([a, d])

answer = 0
wolf, fox = move_wolf(n, graph), move_fox(n, graph)
for i in range(n):
    if fox[i] < wolf[i]:
        answer += 1
print(answer)
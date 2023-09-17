# 서강그라운드
import heapq

def dijkstra(i):
    dist = [1e9]*n
    dist[i] = 0
    Q = [(0, i)]

    while Q:
        d, node = heapq.heappop(Q)

        if d > m or d > dist[node]:
            continue

        dist[node] = d
        for v, w in graph[node]:
            heapq.heappush(Q, (d+w, v))

    return [i for i in range(len(dist)) if dist[i] != 1e9]

n, m, r = map(int, input().split())
item = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1].append((b-1, l))
    graph[b-1].append((a-1, l))

ans = 0
for i in range(n):
    ans = max(ans, sum(item[i] for i in dijkstra(i)))

print(ans)
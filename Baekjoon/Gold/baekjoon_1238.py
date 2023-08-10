import heapq

def dijk(arr, s): # s: 시작하게 되는 지점
    res = [1e9]*n
    res[s] = 0
    pq = [(0, s)]
    while pq: 
        t, i = heapq.heappop(pq)

        if res[i] != t:
            continue

        for j, jt in arr[i]:
            dist = t + jt
            if res[j] > dist:
                res[j] = dist
                heapq.heappush(pq, (dist, j))
    return res

n, m, x = map(int, input().split())
x -= 1
graph = [[]*n for _ in range(n)]
reverse = [[]*n for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a-1].append((b-1, t))
    reverse[b-1].append((a-1, t))

graph_dist = dijk(graph, x) # x로부터 다른 곳까지의 거리
reverse_dist = dijk(reverse, x) # 다른 곳으로부터 x까지의 거리

ans = max([graph_dist[i] + reverse_dist[i] for i in range(n)])
print(ans)
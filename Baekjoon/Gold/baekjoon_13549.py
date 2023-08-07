# 숨바꼭질 3

import heapq

N, K = map(int, input().split())

def sol():
    if N >= K:
        return N-K
    
    visited = [1e9]*100001
    visited[N] = 0
    pq = [(0, N)]

    while pq:
        dist, x = heapq.heappop(pq)

        if visited[x] != dist:
            continue
        
        if x+1 < 100001 and visited[x+1] > dist+1:
            visited[x+1] = dist+1
            heapq.heappush(pq, (dist+1, x+1))
        if x-1 > -1 and visited[x-1] > dist+1:
            visited[x-1] = dist+1
            heapq.heappush(pq, (dist+1, x-1))
        if 2*x < 100001 and visited[2*x] > dist:
            visited[2*x] = dist
            heapq.heappush(pq, (dist, 2*x))
    
    return visited[K]

print(sol())
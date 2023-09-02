def solution(N, road, K):
    arr = [[] for _ in range(N+1)]
    time = [1e9] * (N+1)
    time[1] = 0
    
    for a, b, c in road:
        arr[a].append((b, c))
        arr[b].append((a, c))
        
    pq = [(0, 1)]
    while pq:
        t, x = heapq.heappop(pq)
        
        if time[x] < t:
            continue
            
        for y, _t in arr[x]:
            if time[y] > t + _t:
                time[y] = t + _t
                heapq.heappush(pq, (t+_t, y))
    return sum(map(lambda x: 1 if x <= K else 0, time))

import heapq
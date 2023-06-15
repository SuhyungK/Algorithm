def bfs(N, K):
    queue = [(N, 0)]

    visited[N] = 0
    while queue:
        s, t = queue.pop(0)
        
        if s == K:
            return
        
        if -1<s-1 and t<visited[s-1]:
            queue.append((s-1, t+1))
            visited[s-1] = t+1
        if s+1<100001 and t<visited[s+1]:
            queue.append((s+1, t+1))
            visited[s+1] = t+1
        if s*2<100001 and t<visited[s*2]:
            queue.append((s*2, t))
            visited[s*2] = t
        print(visited[:K])

N, K = map(int, input().split())
visited = [1e9]*100001


bfs(N, K)
print(visited[K])
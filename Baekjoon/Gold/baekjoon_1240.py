# 노드사이의 거리

import collections

def bfs(s, e):
    queue = collections.deque([s])
    visited = collections.defaultdict(int)
    visited[s] = 0

    while queue:
        i = queue.popleft()
        
        for j, dist in grpah[i]:
            if visited[j]:
                continue

            visited[j] = visited[i]+dist
            if j == e:
                return visited[j] 
            queue.append(j)
            
    return visited

n, m = map(int, input().split())
grpah = collections.defaultdict(list)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    grpah[a].append((b, c))
    grpah[b].append((a, c))

for i in range(m):
    print(bfs(*map(int, input().split())))

# ABCDE

N, M =  map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False]*(N)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i, depth):
    if depth == 4:
        return True
    
    visited[i] = True
    for x in graph[i]:
        if not visited[x] and dfs(x, depth+1):
            return True
    visited[i] = False

    return False

def sol():
    for i in range(N):
        if dfs(i, 0):
            return True
    return False

print(int(sol()))
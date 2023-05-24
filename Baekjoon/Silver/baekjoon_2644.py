# 촌수 계산

def bfs(s, t):
    q = [(s, 1)]
    visit = [0]*(N+1)
    visit[s] = 1
    while q:
        s, d = q.pop(0)
        for a in graph[s]:
            if a == t:
                return d
            if not visit[a]:
                visit[a] = 1
                q.append((a, d+1))
    return -1

N = int(input())
s, t = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(s, t))
# 트리의 지름

"""
dfs 함수

now: 현재 노드
cost: ~현재 노드까지의 가중치
visited: 각 노드들까지 가는데 걸리는 가중치
가중치는 양의 정수라고 했으므로, visited의 초기값은 0으로 설정

past: 다음 노드
w: 다음 노드까지 가는데 걸리는 가중치
"""
def dfs(now, cost, visited):
    visited[now] = cost
    
    for past, w in graph[now]:
        if visited[past] == -1:
            visited = dfs(past, cost+w, visited)

    return visited

from collections import defaultdict

# 그래프 초기화
graph = defaultdict(list)

n = int(input())
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

visited1 = [-1]*(n+1)
dist1 = dfs(1, 0, visited1)
a = dist1.index(max(dist1))

visited2 = [-1]*(n+1)
dist2 = dfs(a, 0, visited2)
print(max(dist2))


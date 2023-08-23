# 트리의 지름

"""
스택으로 구현하기
"""

def dfs(i):
    visited = [-1] * (n+1)
    visited[i] = 0
    stack = [i]

    while stack:
        node = stack.pop()

        for past, w in graph[node]:
            if visited[past] == -1:
                visited[past] = visited[node] + w
                stack.append(past)

    return visited

def solution():
    dist = dfs(1)
    return max(dfs(dist.index(max(dist))))

from collections import defaultdict

graph = defaultdict(list)

n = int(input())
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

print(solution())
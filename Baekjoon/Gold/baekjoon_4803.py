# 트리

import sys
from collections import defaultdict
# input = sys.stdin.readline
sys.stdin = open('input.txt')

def dfs(p, i, cycle):
    for c in graph[i]:
        if c == p:
            continue
        if visited[c]:
            return True
        visited[c] = True
        if dfs(i, c, cycle):
            cycle = True
    # print(p, i, cycle, visited)
    return cycle

tc = 1
while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    cnt = 0
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            cnt += not dfs(i, i, False)
        # print(visited, cycle)

    print(f'Case {tc}:', end=' ')
    if cnt == 1:
        print(f'There is one tree.')
    elif cnt == 0:
        print('No trees.')
    else:
        print(f'A forest of {cnt} trees.')
    tc += 1
# 트리와 쿼리

import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dfs(p, c):
    cnt = 0
    for x in graph[c]:
        if p != x:
            cnt += dfs(c, x)
    child[c] = cnt+1
    return cnt+1

graph = defaultdict(list)
N, R, Q = map(int, input().split())
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

child = [0]*(N+1)
dfs(R, R)

for i in range(Q):
    print(child[int(input())])
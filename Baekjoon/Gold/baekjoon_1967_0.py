# 트리의 지름

import sys
from collections import defaultdict
sys.setrecursionlimit(40000)

def dfs(parent):
    ans = 0
    for child, weight in graph[parent]:
        ans = max(ans, dfs(child)+weight)

    return ans

# 그래프 초기화
graph = defaultdict(list)

n = int(input())
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))

ans = 0
for i in range(1, n+1):
    res_lst = sum(sorted([dfs(c) + w for c, w in graph[i]], reverse=True)[:2])
    ans = max(ans, res_lst)

print(ans)
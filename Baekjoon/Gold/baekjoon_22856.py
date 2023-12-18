# 트리 순회

import sys
sys.setrecursionlimit(1000000)

def traversal(i, cnt):
    if tree[i][0] != -1:
        cnt = traversal(tree[i][0], cnt+1) + any(visited)
    visited[i] = False
    if tree[i][1] != -1:
        cnt = traversal(tree[i][1], cnt+1) + any(visited)
    return cnt

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    a, *child = map(int, input().split())
    tree[a].extend(child)

visited = [True] * (N+1)
visited[0] = False
print(traversal(1, 0))
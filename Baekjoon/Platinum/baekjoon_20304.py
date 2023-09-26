# 비밀번호 제작

from collections import deque

MIN = 1e10
N = int(input())
M = int(input())
visited = [MIN]*(N+1)
queue = deque()

lst = list(map(int, input().split()))
for x in lst:
    visited[x] = 0
    queue.append(x)

max_dist, n = 0, len(bin(N))-2
while queue:
    x = queue.popleft()

    for i in range(n):
        nx = x^(1<<i)
        if nx>N or visited[nx] != MIN:
            continue
        visited[nx] = visited[x]+1
        queue.append(nx)
        max_dist = max(max_dist, visited[nx])

print(max_dist)


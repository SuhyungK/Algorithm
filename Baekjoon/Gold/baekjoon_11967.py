# 불켜키

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
room = defaultdict(list)
visited = defaultdict(bool)
light = dict()

for _ in range(m):
    x, y, a, b = map(lambda x: int(x)-1, input().rstrip().split())
    room[(x, y)].append([a, b])

queue = deque([(0, 0)])
light[(0, 0)] = True
visited[(0, 0)] = True
while queue:
    x, y = queue.popleft()

    for nx, ny in room[(x, y)]:
        print(x, y, nx, ny)
        if not light.get((nx, ny)):
            light[(nx, ny)] = True
            if visited[(nx, ny)]:
                queue.append((nx, ny))

    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue

        if not visited[(nx, ny)]:
            visited[(nx, ny)] = True
            if light.get((nx, ny)):
                queue.append((nx, ny))

print(light)
print(len(light))

"""
3 6
1 1 1 2
2 1 2 2
1 1 1 3
2 3 3 1
1 3 1 2
1 3 2 1
"""
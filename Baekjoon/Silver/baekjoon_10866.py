# 덱

import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
for _ in range(int(input())):
    tmp = list(input().split())
    od = tmp[0]

    if od == 'push_front':
        queue.appendleft(tmp[1])
    elif od == 'push_back':
        queue.append(tmp[1])
    elif od == 'pop_front':
        if queue: print(queue.popleft())    
        else: print(-1)
    elif od == 'pop_back':
        if queue: print(queue.pop())
        else: print(-1)
    elif od == 'size':
        print(len(queue))
    elif od == 'empty':
        if queue: print(0)
        else: print(1)
    elif od == 'front':
        if queue: print(queue[0])
        else: print(-1)
    else:
        if queue: print(queue[-1])
        else: print(-1)
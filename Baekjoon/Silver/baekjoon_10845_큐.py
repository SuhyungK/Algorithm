import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

for _ in range(int(input())):
    Input = input().split()
    order = Input[0]

    if order == 'push':
        queue.append(Input[1])
    elif order == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if not queue: print(1)
        else: print(0)
    elif order == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif order == 'back':
        if queue: print(queue[-1])
        else: print(-1)
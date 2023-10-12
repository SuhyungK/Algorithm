# 큐 2

"""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""


import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline
from collections import deque

def _push(x):
    queue.append(x)

def _pop():
    if is_empty():
        return -1
    return queue.popleft()

def size():
    return len(queue)

def is_empty():
    # 비어 있는 경우 True
    return not len(queue)

def front():
    if is_empty():
        return -1
    return queue[0]

def back():
    if is_empty():
        return -1
    return queue[-1]

queue = deque()

N = int(input())
for _ in range(N):
    op, *n = input().split()

    if op == 'push':
        _push(int(n[0]))
    elif op == 'pop':
        print(_pop())
    elif op == 'size':
        print(size())
    elif op == 'front':
        print(front())
    elif op == 'back':
        print(back())
    elif op == 'empty':
        print(int(is_empty()))
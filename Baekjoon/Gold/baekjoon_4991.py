# 로봇 청소기 

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'o':
                return i, j

def find_dirty(arr):
    dirty = {}
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '*':
                dirty[(i, j)] = cnt
                cnt += 1
    return dirty

def bfs(arr, start, dirty):
    visited = [[[False] * (1 << len(dirty)) for _ in range(w)] for _ in range(h)]
    queue = [(*start, 0, 0)]
    target_bitmask = (1 << len(dirty)) - 1
    while queue:
        x, y, cnt, bitmask = queue.pop(0)
        print(x, y, cnt, bin(bitmask)[2:].zfill(2))
        if bitmask == target_bitmask:
            # print(x, y)
            # for row in visited:
            #     print(row)
            return cnt
        
        for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if nx < 0 or ny < 0 or nx >= h or ny >= w or arr[nx][ny] == 'x':
                continue

            if arr[nx][ny] == '*':
                next_bitmask = bitmask | (1 << dirty[(nx, ny)])
                if not visited[nx][ny][next_bitmask]:
                    visited[nx][ny][next_bitmask] = True
                    queue.append((nx, ny, cnt+1, next_bitmask))
            elif not visited[nx][ny][bitmask]:
                visited[nx][ny][bitmask] = True
                queue.append((nx, ny, cnt+1, bitmask))

    return -1

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    ROOM = [list(input()) for _ in range(h)]
    dirty = find_dirty(ROOM)
    print(bfs(ROOM, find_start(ROOM), dirty))


# check_result = []
# while True:
#     Input = int(input())
#     if not Input:
#         break
#     check_result.append(Input)

# for i in range(len(check_result)):
#     if result[i] != check_result[i]:
#         print(i, end=" ")
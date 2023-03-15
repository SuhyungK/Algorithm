# 48ms
# import sys 안 쓴 건 딕셔너리가 더 빠른데 쓰면 리스트가 더 빠른듯?? 

"""
0세대 : 1번
1세대 : 2번
2세대 : 4번
3세대 : 8번

이런식을 도는데 1세대는 1세대 이전(~0세대)까지 돌았던 커브 리스트에서 다 -1 씩 해준만큼 돌고
1세대는 2세대 이전(~1세대)까지 돌았던 커브 리스트를 가져와서 -1씩 해준만큼 도는 거
그래서 애초에 최대 커브 배열을 만들고 커브 리스트에 값을 넣으면서 점도 같이 찍어주기
근데 오래걸려...
"""

import sys
input = sys.stdin.readline

N = int(input())
grid = {}
dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)
next = [-1] * 1025

def curve(x, y, d, g):
    x += dx[d]; y += dy[d]
    grid[(x, y)] = 1
    next[0] = (d+1)%4
    for i in range(g):
        t = 2**i
        for j in range(1, 2**i+1):
            d = next[t-j]
            x += dx[d]; y += dy[d]
            grid[(x, y)] = 1
            next[t+j-1] = (d+1)%4

for _ in range(N):
    x, y, d, g = map(int, input().split())
    grid[(x, y)] = 1
    curve(x, y, d, g)

ans = 0
for x, y in sorted(grid):
    if grid.get((x, y+1)) and grid.get((x+1, y)) and grid.get((x+1, y+1)):
        ans += 1

print(ans)


# --------------------------------------------------------------------- # 


import sys
input = sys.stdin.readline

N = int(input())
grid = {}
dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    grid[(x, y)] = 1
    dir = [d]
    for i in range(g):
        next = []
        for d in dir[::-1]:
            next.append((d+1)%4)
        dir += next
    for d in dir:
        x += dx[d]; y += dy[d]
        grid[(x, y)] = 1

ans = 0
for x in range(100):
    for y in range(100):
        if grid.get((x, y)) and grid.get((x, y+1)) and grid.get((x+1, y)) and grid.get((x+1, y+1)):
            ans += 1

print(ans)

import sys
input = sys.stdin.readline

N = int(input())
grid = {}
dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    grid[(x, y)] = 1
    dir = [d]
    for i in range(g):
        next = []
        for d in dir[::-1]:
            next.append((d+1)%4)
        dir += next

    for d in dir:
        x += dx[d]
        y += dy[d]
        grid[(x, y)] = 1

ans = 0
for x, y in sorted(grid):
    if grid.get((x, y+1)) and grid.get((x+1, y)) and grid.get((x+1, y+1)):
        ans += 1

print(ans)
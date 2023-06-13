import sys
sys.stdin = open('input.txt')

# 원자 소멸 시뮬레이션

import heapq

dx, dy = (0, 0, -0.5, 0.5), (0.5, -0.5, 0, 0)
def annihilation(x1, y1, d1, x2, y2, d2):

    time = 0
    if d1 == 0:
        if d2 == 1 and x1 == x2:
            time = (y2-y1)/2
        elif d2 == 2 and x2-x1 == y2-y1:
            time = x2-x1
        elif d2 == 3 and x1-x2 == y2-y1:
            time = x1-x2
    elif d1 == 1:
        if d2 == 0 and x1 == x2:
            time = (y1-y2)/2
        elif d2 == 2 and x2-x1 == y1-y2:
            time = x2-x1
        elif d2 == 3 and x1-x2 == y1-y2:
            time = x1-x1
    elif d1 == 2:
        if d2 == 0 and x1-x2 == y1-y2:
            time = x1-x2
        elif d2 == 1 and x1-x2 == y2-y1:
            time = x1-x2
        elif d2 == 3 and y1 == y2:
            time = (x1-x2)/2
    elif d1 == 3:
        if d2 == 0 and x2-x1 == y1-y2:
            time = x2-x1
        elif d2 == 1 and x2-x1 == y2-y1:
            time = x2-x1
        elif d2 == 2 and y1 == y2:
            time = (x2-x1)/2

    if time > 0:
        return time
    return 0
        
def sol():
    N = int(input())
    ans = 0
    atom = [tuple(map(int, input().split())) for _ in range(N)]
    
    queue = []
    for i in range(len(atom)):
        x1, y1, d1 = atom[i][:3]
        for j in range(i+1, len(atom)):
            time = annihilation(x1, y1, d1, *atom[j][:3])  
            if time:
                heapq.heappush(queue, (time, i, j))

    # print(queue)
    if queue:
        maxTime = queue[0][0]
        possible = [False for _ in range(len(atom))]
        disappear_atom = set()
        while queue:
            time, i, j = heapq.heappop(queue)
            
            # print(time, i, j, possible, disappear_atom)
            if maxTime < time:
                # print(disappear_atom)
                for idx in disappear_atom:
                    ans += atom[idx][3]
                    possible[idx] = True

                maxTime = time
                disappear_atom = set()

            if possible[i] or possible[j]:
                continue

            disappear_atom.update((i, j))

        for idx in disappear_atom:
            ans += atom[idx][3]
    
    return ans

for tc in range(int(input())):
    print(f'#{tc+1}', sol())

"""
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9
14
-6 5 3 1
-3 5 2 1
-5 2 1 1
3 5 3 1
5 7 1 1
6 7 3 1
7 5 2 1
5 3 0 1
-4 -4 1 1
-4 -6 0 1
5 -3 2 1
4 -6 0 1
6 -4 1 1
9 -7 2 1
"""
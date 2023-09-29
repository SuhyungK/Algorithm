# 낚시왕

import sys
sys.stdin = open('input.txt')

def catch(j):
    for i in range(R):
        if arr[i][j]:
            return i
    return -1

def find_pos(r, c, s, d, z):
    if d == 1:
        if s<=r:
            r -= s
        elif s<=R-1+r:
            r = s-r 
            d = 2
        else:
            r = R-1-(s-(R-1+r))
    elif d == 2:
        if s<=R-1-r:
            r += s
        elif s<=2*(R-1)-r:
            r = R-1-(s-(R-1-r))
            d = 1
        else:
            r = s-2*(R-1)+r
    elif d == 4:
        if s<=c:
            c -= s
        elif s<=C-1+c:
            c = s-c 
            d = 3
        else:
            c = C-1-(s-(C-1+c))
    elif d == 3:
        if s<=C-1-c:
            c += s
        elif s<=2*(C-1)-c:
            c = C-1-(s-(C-1-c))
            d = 4
        else:
            c = s-2*(C-1)+c
    return r, c, s, d, z

def move(arr):
    tmp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j]:
                r, c, s, d, z = find_pos(i, j, *arr[i][j])
                # print(i, j, r, c, s, d, z)
                # for row in tmp:
                #     print(row)
                if tmp[r][c] and tmp[r][c][2] > z:
                    continue
                tmp[r][c] = [s, d, z]
    return tmp

R, C, M = map(int, input().split())
arr = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d in (1, 2):
        s %= 2*(R-1)
    else:
        s %= 2*(C-1)
    arr[r-1][c-1] = [s, d, z]

res = 0
for j in range(C):
    i = catch(j)
    if i != -1:
        res += arr[i][j][2]
        arr[i][j] = []
    arr = move(arr)

print(res)
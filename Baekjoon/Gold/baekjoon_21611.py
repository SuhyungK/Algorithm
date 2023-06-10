# 마법사 상어와 블리자드
import sys
sys.stdin = open('input.txt')

def makeMagirDir():
    global dir
    _dir = {1: [1], 2: [3], 3: [5], 4: [7]}
    
    d = 3
    while d<N:
        _dir[1].append(_dir[4][-1]+d)
        d += 1
        k = 2
        while k<5:
            _dir[k].append(_dir[k-1][-1]+d)
            k += 1
        d += 1
    
    dir = [0, _dir[4], _dir[2], _dir[1], _dir[3]]

def makeList():
    u, v = 1, -1 # u : 이동 거리 확장, v: 이동 방향 변경
    x, y = N//2, N//2
    lst = [-1]
    while True:
        if y+(u*v)+v < 0:
            lst.extend(arr[x][y+v::v])
        else: 
            lst.extend(arr[x][y+v:y+(u*v)+v:v])
        y += u*v
        v *= -1

        if u == N:
            return lst

        if x+(u*v)+v < 0:
            lst.extend([row[y] for row in arr[x+v::v]])
        else:
            lst.extend([row[y] for row in arr[x+v:x+(u*v)+v:v]])
        x += u*v
        u += 1

def blizzard(d, s):
    global lst
    for t in dir[d][:s][::-1]:
        lst = lst[:t]+lst[t+1:]

def explode_move():
    global ans, lst
    while True:
        i, l = 1, len(lst)
        while i<len(lst)-3:
            if lst[i] == 0:
                break

            if len(set(lst[i:i+4])) > 1:
                i += 1
                continue
            
            j = 1
            while len(set(lst[i:i+4+j])) == 1:
                # print(i, j, lst)
                j += 1

            ans += lst[i]*(3+j)
            lst = lst[:i]+lst[i+3+j:]
        
        if l == len(lst):
            break

def change():
    global lst
    tmp = [-1]
    i = 1
    while i<len(lst) and lst[i] != 0:

        j = 1
        while i+j<=len(lst) and len(set(lst[i:i+j])) == 1:
            j += 1

        tmp.extend([j-1, lst[i]])
        i += j-1
        # print(tmp)

    lst = tmp + [0]*(N*N-len(lst))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = []
ans = 0

makeMagirDir()
lst = makeList()
for _ in range(M):
    d, s = map(int, input().split())
    print('1', lst)
    blizzard(d, s)
    print('2', lst)
    explode_move()
    print('3', lst)
    change()
    lst = lst[:N*N]
    print('4', lst)

print(ans)
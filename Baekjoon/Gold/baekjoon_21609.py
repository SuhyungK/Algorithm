import sys
sys.stdin = open('input.txt')

# 상어 중학교

# 반시계 방향의 회전
def rotate(arr):
    return list(map(list, zip(*arr)))[::-1]

# bfs로 블럭 탐색
def bfs(si, sj, v, cnt):
    v[si][sj], t = cnt, block[si][sj]
    Q, idx, rbw = [(si, sj)], 0, 0
    while idx < len(Q):
        i, j = Q[idx]

        for ni, nj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if -1<ni<N and -1<nj<N and (b:=block[ni][nj])>=0:
                if b == 0 and v[ni][nj] != cnt:
                    v[ni][nj] = cnt
                    Q.append((ni, nj))
                    rbw += 1
                
                elif b==t and v[ni][nj] == 0:
                    v[ni][nj] = cnt
                    Q.append((ni, nj))

        idx += 1
    return [len(Q), rbw, si, sj, Q]

# 블럭의 집합 찾기
def find_blockgroup():
    v = [[0]*N for _ in range(N)]
    max_blocks = [0, 0, -1, -1, []]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if block[i][j]>0 and not v[i][j]:
                cnt += 1
                max_blocks = max(max_blocks, bfs(i, j, v, cnt))
                print(max_blocks)

    return max_blocks[-1]

# 그룹 제거 + 점수 합산
def remove(blocks):
    global res

    res += len(blocks) ** 2
    for br, bc in blocks:
        block[br][bc] = -2

# 중력 작용
def gravity(arr):
    for j in range(N):
        bot = i = N-1
        while -1<i:
            t = arr[i][j]
            if t == -1:
                bot = i-1
            elif t>=0:
                if bot > i:
                    arr[bot][j] = t
                    arr[i][j] = -2
                bot -= 1
            i -= 1
    return arr

def autoplay():
    global block
    while 1:
        blocks = find_blockgroup()
        if len(blocks) <= 1:
            return
        # print(blocks)
        remove(blocks)
        gravity(block)
        block = gravity(rotate(block))

        print()
        for row in block:
            print(*row)
        print()

N, M = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (0, 1, 0, -1), (-1, 0, 1, 0)
res = 0

autoplay()
print(res)
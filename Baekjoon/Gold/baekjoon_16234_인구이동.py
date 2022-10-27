import sys
sys.stdin = open('test.txt')

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

dic = {}
for r in range(N):
    for c in range(N):
        dic[(r, c)] = (r, c)

Q = {}
# while Q:
#     Q = {}
for k, v in dic.items():
    r, c = k
    if dic[(r, c)] == (r, c):
        q = [(r, c)]
        Q[(r, c)] = arr[r][c]
        cnt = 1
        while q:
            rr, cc = q.pop(0)
            for i in range(4):
                nr, nc = rr + dr[i], cc + dc[i]
                if dic.get((nr, nc)) and dic.get((nr, nc)) != (r, c) and L <= abs(arr[rr][cc] - arr[nr][nc]) <= R:
                    dic[(nr, nc)] = (r, c)
                    Q[(r, c)] += arr[nr][nc]
                    cnt += 1
            print(Q)
        Q[(r, c)] //= cnt 

    
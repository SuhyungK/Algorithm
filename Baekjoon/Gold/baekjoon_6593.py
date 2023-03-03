<<<<<<< HEAD
import sys
sys.stdin = open('input.txt')

def start(L, R, C):
    for i in range(L*R):
        for j in range(C):
            if build[i][j] == 'S':
                return i, j

def bfs(build, L, R, C):
    sr, sc = start(L, R, C)
    build[sr][sc] = 0
    q = [(sr, sc)]
    while q:
        r, c = q.pop(0)
        for dr, dc in (-R, 0), (R, 0), (-1, 0), (1, 0), (0, 1), (0, -1):
            # if not ((dr, dc) == (-1, 0) and r % R == 0) or ((dr, dc) == (1, 0) and (r+1) % R == 0):
            if not ((dr, dc) == (-1, 0) and r % R == 0) or ((dr, dc) == (1, 0) and (r+1) % R == 0):
                if -1 < (nr:=r + dr) < L * R and -1 < (nc:=c + dc) < C:
                    if build[nr][nc] == 'E':
                        return f'Escaped in {build[r][c] + 1} minute(s).'
                    elif build[nr][nc] == '.':
                        build[nr][nc] = build[r][c] + 1
                        q.append((nr, nc))
    return 'Trapped!'

while 1:
    if (p:=input()) == '0 0 0':
        break
    L, R, C = map(int, p.split())
    build = list(map(lambda x: list(x), ' '.join(input() for _ in range(L*(R+1))).split()))
    
    print(bfs(build, L, R, C))
=======
while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break
    building = [list(p) if (p:=input()) else for _ in range(L * (R+1))]
    
    for i in range(R):
>>>>>>> c585bf6 (merge전)

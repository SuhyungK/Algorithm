# 새로운 게임 2

def move(nr, nc, tmp):
    global arr, is_finish
    start_h = len(arr[nr][nc])
    arr[nr][nc].extend(tmp)
    if len(arr[nr][nc]) >= 4:
        is_finish = True
    for new_h, x in enumerate(tmp, start_h):
        piece[x] = [nr, nc, piece[x][2], new_h]

def judge(i, no_recur=False):
    global piece, arr
    r, c, d, h = piece[i]

    nr = r + DIR[d][0]
    nc = c + DIR[d][1]

    if not(0 <= nr < N and 0 <= nc < N) or (CHESS[nr][nc] == 2 and not no_recur):
        piece[i][2] = DIR_REVERSE[d]
        judge(i, True)
        return 
    
    tmp = arr[r][c][h:]
    arr[r][c] = arr[r][c][:h]
    if CHESS[nr][nc] == 1:
        tmp.reverse()

    if CHESS[nr][nc] == 2 and no_recur:
        nr, nc = r, c
    
    move(nr, nc, tmp)

def game():
    global arr, piece
    for i in range(1, K+1):
        judge(i)
        if is_finish:
            return 

N, K = map(int, input().split())
CHESS = [list(map(int, input().split())) for _ in range(N)]
DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
DIR_REVERSE = [1, 0, 3, 2]
piece = dict()
arr = [[[] for _ in range(N)] for _ in range(N)]
is_finish = False

for i in range(1, K+1):
    r, c, d = map(int, input().split())
    piece[i] = [r-1, c-1, d-1, 0] # 행, 열, 방향, 쌓여 있는 위치
    arr[r-1][c-1].extend([i])

turn = 0
while turn <= 1000:
    game()
    turn += 1
    if is_finish:
        break
        
if turn == 1001:
    turn = -1
print(turn) 
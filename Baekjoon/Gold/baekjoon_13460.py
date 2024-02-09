# 구슬 탈출

def move(this_x, this_y, other_x, other_y, d, is_red):
    global is_blue_in_hole, is_red_in_hole

    while True: 
        next_x = this_x + direction[d][0]
        next_y = this_y + direction[d][1]
        if board[next_x][next_y] == "#" or (next_x == other_x and next_y == other_y):
            return this_x, this_y
        elif board[next_x][next_y] == "O":
            if is_red:
                is_red_in_hole = True
            else:
                is_blue_in_hole = True
            return (-1, -1)
        
        this_x = next_x
        this_y = next_y

def up(R, B):
    if R[0] <= B[0]:
        R = move(*R, *B, 0, True)
        B = move(*B, *R, 0, False)
    else:
        B = move(*B, *R, 0, False)
        R = move(*R, *B, 0, True)
    return R, B

def down(R, B):
    if R[0] >= B[0]:
        R = move(*R, *B, 1, True)
        B = move(*B, *R, 1, False)
    else:
        B = move(*B, *R, 1, False)
        R = move(*R, *B, 1, True)
    return R, B

def right(R, B):
    if R[1] >= B[1]:
        R = move(*R, *B, 2, True)
        B = move(*B, *R, 2, False)
    else:
        B = move(*B, *R, 2, False)
        R = move(*R, *B, 2, True)
    return R, B

def left(R, B):
    if R[1] <= B[1]:
        R = move(*R, *B, 3, True)
        B = move(*B, *R, 3, False)
    else:
        B = move(*B, *R, 3, False)
        R = move(*R, *B, 3, True)
    return R, B

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
direction = ((-1, 0), (1, 0), (0, 1), (0, -1))

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            R = (i, j)
            board[i][j] = "."
        elif board[i][j] == "B":
            B = (i, j)
            board[i][j] = "."

is_red_in_hole = False
is_blue_in_hole = False

def sol(R, B):
    move_fn = {
        0: (lambda x: up(x[0], x[1])),
        1: (lambda x: down(x[0], x[1])),
        2: (lambda x: right(x[0], x[1])),
        3: (lambda x: left(x[0], x[1]))
    }
    visited = {(R, B): True}
    queue = [(R, B, 0)]
    while queue:
        R, B, cnt = queue.pop(0)
        # print(R, B, cnt)
        if cnt >= 10:
            return -1

        for k in range(4):
            new_R, new_B = move_fn[k]((R, B))

            if not visited.get((new_R, new_B)):
                visited[(new_R, new_B)] = True
                queue.append((new_R, new_B, cnt+1))

            if new_R == (-1, -1) and new_B != (-1, -1):
                return cnt + 1
    
    return -1

print(sol(R, B))
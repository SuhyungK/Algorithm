# 2048 (Easy)

def rotate(dir, board):
    if dir == 1: # UP
        arr = move(list(map(list, zip(*board))))
        return list(map(list, zip(*arr)))
    elif dir == 2: # DOWN
        arr = move(list(map(list, zip(*board[::-1]))))
        return list(map(list, zip(*arr)))[::-1]
    elif dir == 3: # RIGHT
        arr = move(row[::-1] for row in board)
        return [row[::-1] for row in arr]
    else: # LEFT
        return move(board)
    
def move(board):
    arr = []
    for row in board:
        i = -1
        tmp = []
        while i<N-1:
            i += 1
            if not row[i]:
                continue
            j = i
            while j<N-1:
                j += 1
                if not row[j]:
                    continue
                if row[j] == row[i]:
                    tmp.append(2*row[i])
                    i = j
                    break
                if row[j] != row[i]:
                    tmp.append(row[i])
                    i = j-1
                    break
            else:
                tmp.append(row[i])
                break
        arr.append(tmp+[0]*(N-len(tmp)))
    return arr

def game(round, board):
    global answer
    if round == 5:
        for row in board:
            answer = max(answer, max(row))
        return 

    for d in range(4):
        tmp = rotate(d, [row[:] for row in board])
        game(round+1, tmp)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
game(0, board)
print(answer)
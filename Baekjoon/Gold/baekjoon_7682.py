def win(s, board):
    if board[0] == board[4] == board[8] == s:
        return True
    if board[2] == board[4] == board[6] == s:
        return True
    for i in (0, 3, 6):
        if board[i] == board[i+1] == board[i+2] == s:
            return True
    for j in range(3):
        if board[j] == board[j+3] == board[j+6] == s:
            return True
    return False

def game(board):
    x_count = board.count('X')
    o_count = board.count('O')

    x_wins = win('X', board)
    o_wins = win('O', board)

    if x_count == o_count+1 and x_wins and not o_wins:
        return True
    if x_count == o_count and not x_wins and o_wins:
        return True
    if not x_wins and not o_wins and x_count == 5 and o_count == 4:
        return True
    return False

while True:
    board = input()
    if board == 'end':
        break
    if game(board):
        print('valid')
    else:
        print('invalid')
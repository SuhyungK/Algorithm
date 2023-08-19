def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j])+1
    
    answer = 0
    for row in board:
        answer = max(answer, max(row))

    return answer**2
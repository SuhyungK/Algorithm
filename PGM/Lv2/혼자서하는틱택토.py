"""
!예외 상황

1. O의 개수가 X+1보다 크거나 같은 게 아닌 경우 
2. 누군가 이겼고 거기서 게임 진행이 종료된 경우
    - O가 이겼고 O의 개수 = X의 개수 + 1
    - X가 이겼고 O의 개수 = X의 개수
(예제에서처럼 누가 이긴다고 해서 무조건 실패한 경우는 아님)
"""


def solution(board):
    answer = -1
    
    # o,x의 개수 세기
    o = sum([row.count('O') for row in board])
    x = sum([row.count('X') for row in board])
    
    def check(lst):
        _set = set(lst)
        winner = ''
        if _set == {'O'}:
            winner = 'O'
        elif _set == {'X'}:
            winner = 'X'
        else:
            return False
        
        print(_set, o, x)
        if winner == 'O' and o != x+1:
            return True
        if winner == 'X' and o != x:
            return True
        return False
        
        
    # 불가능한 경우
    if o < x or o > x+1:
        return 0
    
    # 가로, 세로, 대각선을 비교하면서 2번 지켜지는지 확인
    dia1, dia2 = [], []
    for i in range(3):
        rows = board[i]
        cols = board[0][i]+board[1][i]+board[2][i]
        
        # 행, 열에 완성된 게 있고 경기가 제대로 진행된 건지 확인
        if check(rows) or check(cols):
            print(check(rows), check(cols))
            return 0
        
        dia1 += board[i][i]
        dia2 += board[i][2-i]
        
    if check(dia1) or check(dia2):
        return 0

    return 1
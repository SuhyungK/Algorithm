# 리코쳇로봇

def wrap_array(board):
    tmp_row = ['D'] * (len(board[0]) + 2)
    ex_board = [['D'] + list(row) + ['D'] for row in board]
    return [['D'] * (len(board[0]) + 2)] + ex_board + [['D'] * (len(board[0]) + 2)]
    
def find_start(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            if arr[i][j] == 'R':
                return (i, j)

def bfs(arr, sr, sc):
    n, m = len(arr), len(arr[0])
    visit = [[1000] * m for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    visit[sr][sc] = 0
    queue = [(sr, sc, 0), (sr, sc, 1), (sr, sc, 2), (sr, sc, 4)]
    while queue:
        r, c, d = queue.pop(0)
        print(r, c, d)
        for i in range(1, 4):
            d = (d+i) % 4
            nr, nc = r, c
            while arr[nr+dr[d]][nc+dc[d]] != 'D':
                nr, nc = nr+dr[d], nc+dc[d]
                
            if arr[nr][nc] == 'G':
                return visit[r][c] + 1
            
            if visit[nr][nc] > visit[r][c] + 1:
                visit[nr][nc] = visit[r][c] + 1
                queue.append((nr, nc, d))

        print()
        for row in visit:
            print(row)
        print()
    return -1
    
def solution(board):
    
    ex_board = wrap_array(board)
    answer = bfs(ex_board, *find_start(ex_board))
    
    return answer

print(solution(["...D...", ".D.G.R.", "....D.D", "D....D.", "..D...."]))
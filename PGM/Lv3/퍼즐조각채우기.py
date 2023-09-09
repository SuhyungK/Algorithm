def solution(game_board, table):
    answer = 0
	
    # 시계 방향 90도 회전
    def rotate(arr):
        return list(map(list, zip(*arr[::-1])))

	# dfs 그래프 탐색
    def dfs(arr, i, j, block):
        if i<0 or j<0 or i>=len(arr) or j>=len(arr[0]) or [i, j] in block or not arr[i][j]:
            return block

        arr[i][j] = 0
        block.append([i, j])
        block = dfs(arr, i-1, j, block)
        block = dfs(arr, i+1, j, block)
        block = dfs(arr, i, j-1, block)
        block = dfs(arr, i, j+1, block)

        return block
	
    # 2차원 배열로 만들기
    def make_block(block):
        row_min, col_min = map(min, zip(*block))
        for i in range(len(block)):
            block[i][0] -= row_min
            block[i][1] -= col_min

        row_max, col_max = map(max, zip(*block))
        arr = [[0]*(col_max+1) for _ in range(row_max+1)]

        for r, c in block:
            arr[r][c] = 1

        return arr, len(block)
	
    # 빈 칸에 맞는 퍼즐 조각 찾기
    def puzzle_block(block, cnt):
        for _ in range(4):
            if blocks[str(block)]:
                blocks[str(block)] -= cnt
                return cnt
            block = rotate(block)

        return 0
	
    # 퍼즐 조각의 모양이 문자열 형태로 저장됨
    # 각 칸의 개수를 값으로 가짐
    blocks = defaultdict(int)
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j]:
                block, cnt = make_block(dfs(table, i, j, []))
                blocks[f"{block}"] += cnt

    game_board = list(map(lambda x: list(map(lambda y: 0 if y else 1,x)) ,game_board))
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j]:
                answer += puzzle_block(*make_block(dfs(game_board, i, j, [])))

    return answer

from collections import defaultdict
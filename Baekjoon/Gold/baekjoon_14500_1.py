# 테트로미노

import sys
input = sys.stdin.readline

def solution():
    def find_block(r, c, block_cnt, block_sum):
        global max_sum
        if block_sum + (4-block_cnt)*max_x < max_sum:
            return 
        
        if block_cnt == 4:
            max_sum = max(max_sum, block_sum)
            return
        
        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if -1<nr<N and -1<nc<M and not visited[nr][nc]:
                visited[nr][nc] = 1
                if block_cnt == 2:
                    find_block(r, c, block_cnt+1, block_sum+paper[nr][nc])
                find_block(nr, nc, block_cnt+1, block_sum+paper[nr][nc])
                visited[nr][nc] = 0
        # for k in range(4):
        #     nr, nc = r+dr[k], c+dc[k]
        #     if -1<nr<N and -1<nc<M and not visited[nr][nc]:
        #         find_block()

    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            find_block(i, j, 1, paper[i][j])
            visited[i][j] = 0
    
    return max_sum

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for __ in range(M)] for _ in range(N)]
dr, dc = (1, 0, -1, 0), (0, 1, 0, -1)
max_x = max(map(max, paper))
max_sum = 0
print(solution())
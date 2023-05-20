# 테트로미노

import sys
input = sys.stdin.readline

def _print():
    print()
    for row in visited:
        print(*row)
    print()

def tetromino(r, c, sum_nums, k):
    global max_sum

    if k == 4:
        if max_sum < sum_nums:
            max_sum = sum_nums
            print(max_sum)
            _print()
        return 
    
    if sum_nums + maxx * (4-k) < max_sum:
        return 
    
    if r+1<N and not visited[r+1][c]:
        visited[r+1][c] = 1
        tetromino(r+1, c, sum_nums+paper[r+1][c], k+1)
        visited[r+1][c] = 0
    if c+1<M and not visited[r][c+1]:
        visited[r][c+1] = 1
        tetromino(r, c+1, sum_nums+paper[r][c+1], k+1)
        visited[r][c+1] = 0
    if -1<r-1 and not visited[r-1][c]:
        visited[r-1][c] = 1
        tetromino(r-1, c, sum_nums+paper[r-1][c], k+1)
        visited[r-1][c] = 0
    if -1<c-1 and not visited[r][c-1]:
        visited[r][c-1] = 1
        tetromino(r, c-1, sum_nums+paper[r][c-1], k+1)
        visited[r][c-1] = 0
    
def main():
    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            tetromino(i, j, paper[i][j], 1)
            if i+2<N:
                visited[i+1][j], visited[i+2][j] = 1, 1
                tetromino(i+1, j, paper[i][j]+paper[i+1][j]+paper[i+2][j], 3)
                visited[i+1][j], visited[i+2][j] = 0, 0

            if j+2<M:
                visited[i][j+1] = visited[i][j+2] = 1
                tetromino(i, j+1, paper[i][j]+paper[i][j+1]+paper[i][j+2], 3)
                visited[i][j+1] = visited[i][j+2] = 0
            visited[i][j] = 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    max_sum = 0
    maxx = max(sum(paper,[]))
    main()
    print(max_sum)



# for i in range(N):
#     for j in range(M):
#         if i+1<N:
#             lst = [[i, j], [i+1, j]]
#             tetromino(lst, i+1, j, paper[i][j]+paper[i+1][j])
#             if i+2<N:
#                 lst.append([i+2, j])
#                 tetromino(lst, i+1, j, paper[i][j]+paper[i+1][j]+paper[i+2][j])
#         if j+1<M:
#             lst = [[i, j], [i, j+1]]
#             tetromino(lst, i, j+1, paper[i][j]+paper[i][j+1])
#             if j+2<M:
#                 lst.append([i, j+2])
#                 tetromino(lst, i, j+1, paper[i][j]+paper[i][j+1]+paper[i][j+2])
        
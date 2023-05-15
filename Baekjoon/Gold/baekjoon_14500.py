# 테트로미노

def tetromino(lst, r, c, sum_nums):
    global max_sum

    if len(lst) == 4:
        if max_sum < sum_nums:
            print(lst, sum_nums)
            max_sum = sum_nums
        return 
    
    if r+1<N and [r+1, c] not in lst:
        tetromino(lst+[[r+1,c]], r+1, c, sum_nums+paper[r+1][c])
    if c+1<M and [r, c+1] not in lst:
        tetromino(lst+[[r,c+1]], r, c+1, sum_nums+paper[r][c+1])
    if -1<r-1 and [r-1, c] not in lst:
        tetromino(lst+[[r-1,c]], r-1, c, sum_nums+paper[r-1][c])
    if -1<c-1 and [r, c-1] not in lst:
        tetromino(lst+[[r,c-1]], r, c-1, sum_nums+paper[r][c-1])
    

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

for i in range(N):
    for j in range(M):
        if i+1<N:
            lst = [[i, j], [i+1, j]]
            tetromino(lst, i+1, j, paper[i][j]+paper[i+1][j])
        if j+1<M:
            lst = [[i, j], [i, j+1]]
            tetromino(lst, i, j+1, paper[i][j]+paper[i][j+1])

print(max_sum)
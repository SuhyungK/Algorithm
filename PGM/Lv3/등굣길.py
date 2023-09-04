def solution(m, n, puddles):
    arr = [[0]*n for _ in range(m)]
        
    arr[0][0] = 1
    for i in range(m):
        for j in range(n):
            if [i+1, j+1] in puddles:
                continue
            if i>0:
                arr[i][j] += arr[i-1][j]
            if j>0:
                arr[i][j] += arr[i][j-1]
            arr[i][j] %= 1000000007
            
    for row in arr:
        print(row)
    return arr[-1][-1]
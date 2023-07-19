def solution(arr1, arr2):
    
    n, m = len(arr1), len(arr2[0])
    answer = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            answer[i][j] = sum([arr1[i][x]*arr2[x][j] for x in range(len(arr2))])
    
    return answer
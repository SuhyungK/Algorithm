def solution(n):
    answer = 0
    cols = [False]*n
    chess = [-1] * n

    def queen(row):
        nonlocal answer
        if row == n:
            answer += 1
            return 

        for c in range(n):
            if cols[c]:
                continue

            for r in range(row+1):
                if chess[row-r] in (c-r, c+r):
                    break
            else:            
                chess[row] = c
                cols[c] = True
                queen(row+1)
                cols[c] = False
                chess[row] = -1

    queen(0)
    return answer
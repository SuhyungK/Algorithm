def compare(a, b):
    if a[::-1] > b[::-1]:
        return a
    return b

def solution(n, info):
    def dfs(i, n, score, arrow): # i: 현재 쏜 과녁 번호, n: 남은 화살 횟수, score: 점수 차이, arrow: 쏜 화살 개수
        nonlocal ans
        if n < 0:
            return
        
        if i == 10 or n == 0:
            arrow += [0] * (10-i)
            arrow.extend([n, score])
            ans = compare(arrow[:], ans)
            return 

        if info[i]:
            dfs(i+1, n-info[i]-1, score+2*(10-i), arrow+[info[i]+1])
        else:
            dfs(i+1, n-1, score+10-i, arrow+[1])
        dfs(i+1, n, score, arrow+[0])

    
    ans, tmp, score = [-1]*12, [], -sum(10-i for i in range(11) if info[i])
    dfs(0, n, score, [])

    if ans[-1] <= 0:
        return [-1]
    return ans[:-1]
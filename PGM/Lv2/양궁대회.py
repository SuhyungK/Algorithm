def solution(n, info):
    answer = []
    
    # 어피치의 점수
    peach = sum([10-i if info[i] else 0 for i in range(11)])
    
    ryanInfo, diff = [0]*11, 0
    
    # i: 배열 인덱스, n: 라이언의 횟수, ryan: 라이언의 점수, peach: 어피치의 점수
    def calc(i, n, ryan, peach): 
        nonlocal diff, answer, ryanInfo
        if n < 0:
            return 
        
        # 라이언이 과녁을 다 쐈으면
        if i<0 or n == 0:
            ryanInfo[-1] += n
            if ryan-peach > diff:
                print(n, ryan, peach, ryanInfo)
                answer = ryanInfo[:]
                diff = ryan-peach
            ryanInfo[-1] -= n
            return 
        
        p = info[i]+1
        if p>1:
            ryanInfo[i] = p
            calc(i-1, n-p, ryan+10-i, peach-10+i)
            ryanInfo[i] = 0
            calc(i-1, n, ryan, peach)
        else:
            ryanInfo[i] = 1
            calc(i-1, n-1, ryan+10-i, peach)
            ryanInfo[i] = 0
            calc(i-1, n, ryan, peach)
    
    calc(10, n, 0, peach)
    
    if answer == []:
        return [-1]
    return answer
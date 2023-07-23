def solution(plans):
    answer = []
    
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = int(h)*60+m
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x: x[1])
    plans.append([" ", 1e13, 0])
    
    now, idx = plans[0][1], 0
    while idx < len(plans)-1:
        next = plans[idx+1][1]
        # 과제 수행 시간이 다음 과제 시작 시간을 넘어선다면
        # 일부만 수행하고 다음 과제부터 시작
        if now + plans[idx][2] > next:
            plans[idx][2] -= (next-now)
            idx += 1
            now = next
            continue
        
        _subject, _, _playtime = plans.pop(idx)
        answer.append(_subject)
        # 현재 과제 수행하고 now 업데이트
        now += _playtime
        if idx > 0:
            idx -= 1
        else:
            now = plans[idx][1]
        
            
    return answer
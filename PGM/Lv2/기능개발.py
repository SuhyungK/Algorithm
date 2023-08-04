def solution(progresses, speeds):
    answer = []
    
    # 배포까지 걸리는 시간 계산
    def calc(idx):
        return math.ceil((100-progresses[idx])/speeds[idx])
    
    # 아직 배포되지 않은 progress의 배포에 걸리는 시간(time)보다
    # 더 적게 걸린다면 같이 배포
    # 더 많이 걸린다면 배포에 걸리는 시간을 변경하고 count를 추가
    time, count = calc(0), 0
    for idx in range(len(progresses)):
        if time >= calc(idx):
            count += 1
        else:
            time = calc(idx)
            answer.append(count)
            count = 1
            
    answer.append(count)
    return answer

import math
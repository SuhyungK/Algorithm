def solution(queue1, queue2):
	# 두 개의 큐를 하나의 큐(Q)로 연결
    Q = queue1 + queue2
    Q1 = sum(queue1)
    
    # 합이 홀수인 경우는 볼가
    if sum(Q) % 2:
        return -1
    
    target = sum(Q)//2
    l = len(queue1)
    i, j = 0, l
    # l은 작은 큐의 길이이다. 2*l은 Q의 길이
    while i < 2*l-1 and j < 4*l:
    	# 타겟 목표에 도달하면 현재까지 이동한 거리를 인덱스 값을 통해 반환
        # i는 시작이 0이므로 그냥 반환
        # j는 시작이 l이었으므로 반환할 때는 l만큼 빼줘야 실제 이동된 순수 거리 값만 반환
        if Q1 == target:
            return i+j-l
        elif Q1 < target:
            Q1 += Q[j%(2*l)] # 순환 큐 형태
            j += 1
        elif Q1 > target:
            Q1 -= Q[i%(2*l)]
            i += 1
    return -1
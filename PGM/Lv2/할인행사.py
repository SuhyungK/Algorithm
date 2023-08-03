def solution(want, number, discount):
	# 키 : 원하는 품목, 값 : 인덱스
    stuff = {want[idx]: idx for idx in range(len(want))}
    answer = 0
    
    # 10일 간 할인하는 품목들에 대해 연산
    # 품목이 stuff 키 값으로 존재한다면 인덱스를 구해 discount_stuff 배열에 추가
    discount_stuff = [0] * len(want)
    for i in range(10):
        idx = stuff.get(discount[i])
        if idx != None:
            discount_stuff[idx] += 1
    
    for i in range(10, len(discount)):
    	# 원하는 품목과 할인하는 품목의 개수가 일치하는 경우
        if discount_stuff == number:
            answer += 1
        
        # 다음날 빠져야 되는 품목과 다음날 추가되는 품목이 같은 거라면
        # 다음에 이행되는 연산을 수행할 필요가 없으므로 넘어감
        if discount[i] == discount[i-10]:
            continue
            
        # 다음날 추가되어야 할 품목을 더해주고
        next_idx = stuff.get(discount[i])
        if next_idx != None:
            discount_stuff[next_idx] += 1
        
        # 10일 전의 품목은 제외하기
        pre_idx = stuff.get(discount[i-10])
        if pre_idx != None:
            discount_stuff[pre_idx] -= 1
    
    if discount_stuff == number:
        answer += 1
    return answer
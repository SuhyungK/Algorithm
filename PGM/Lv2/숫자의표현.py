def solution(n):
    answer = 0
    start = 1
    
	# 1부터 시작해서 연속한 숫자들을 더해나가는 풀이
    while start <= n:
        sum = x = start
        while sum <= n:
        
        	# 더한 값이 n이 되면 answer 증가 후 break
            if sum == n:
                answer += 1
                break
            x += 1
            sum += x
        
        # 더하기가 시작되는 값 증가
        start += 1
    return answer
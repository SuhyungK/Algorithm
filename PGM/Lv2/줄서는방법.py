def solution(n, k):
    answer = []
    order = [x for x in range(1, n+1)]
    
    # 팩토리얼 배열을 만들어서 미리 구해놓기
    factorial = [0]*(n-1)
    factorial[0] = 1
    
    for i in range(1, n-1):
        factorial[i] = factorial[i-1] * (i+1)
    
    k -= 1
    for factor in factorial[::-1]:
        answer.append(order.pop(k//factor))
        k %= factor
        if k == 0:
            return answer + order
        
    return answer
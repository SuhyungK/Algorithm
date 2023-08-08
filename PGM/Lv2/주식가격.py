def solution(prices):
    L = len(prices)
    answer = [0] * L
    
    stack = []
    for i, x in enumerate(prices):
        while stack and stack[-1][1] > x:
            idx = stack.pop()[0]
            answer[idx] = i-idx
        stack.append((i, x))
        
    while stack:
        idx = stack.pop()[0]
        answer[idx] = L-1-idx
        
    return answer
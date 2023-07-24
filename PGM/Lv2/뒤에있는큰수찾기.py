def solution(numbers):
    L = len(numbers)
    answer = [-1]*L
    
    for i in range(L-2, -1, -1):
        j = i + 1
        while j < L:
            if numbers[i] < numbers[j]:
                answer[i] = numbers[j]
                break
            
            if answer[j] == -1:
                answer[i] = -1
                break
            
            if numbers[i] < answer[j]:
                answer[i] = answer[j]
                break
                
            j += 1
            
    return answer
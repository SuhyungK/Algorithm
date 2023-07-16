def solution(elements):
    L = len(elements)
    
    elements += elements
    answer = set()
    
    for start in range(L):
        for next_index in range(start, start+L):
            answer.add(sum(elements[start:next_index+1]))
        
    return len(answer)
def solution(weights):
    answer = 0
    
    weight = Counter(weights)
    
    print('weight', weight)
    def balance(n):
        people = 0
        for x in (n*2/3, n*2/4, n*3/2, n*3/4, n*4/2, n*4/3):
            if weight[x]:
                people += weight[x]
        
        people += (weight[n]-1)
        return weight[n] * people
    
    for key in weight:
        print(balance(key))
        answer += balance(key)
        
    return answer//2

from collections import Counter
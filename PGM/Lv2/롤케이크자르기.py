def solution(topping):
    answer = 0
    
    count1, count2 = defaultdict(int), Counter(topping)
    for i in range(len(topping)):
        top = topping[i]
        count2[top] -= 1
        count1[top] += 1
        if not count2[top]:
            del count2[top]
        if len(count1.keys()) == len(count2.keys()):
            answer += 1
    
    return answer
from collections import Counter, defaultdict
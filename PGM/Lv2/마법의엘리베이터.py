def solution(storey):
    
    Q = deque([(storey, 1, 0)])
    answer = 1e9
    limit = 10 ** len(str(storey))
    while Q:
        story, c, push = Q.popleft()
        
        if story == 0:
            answer = min(answer, push)
            continue
        
        x = story % (10**c)
        step = int(str(x)[0])
        
        if 0<=story-x:
            Q.append((story-x, c+1, push+step))
        if story+(10**c-x)<=limit:
            Q.append((story+10**c-x, c+1, push+10-step))
    
    return answer

from collections import deque
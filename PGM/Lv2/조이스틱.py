def control(s):
    return min(ord(s)-65, 91-ord(s))

def solution(name):
    name = list(name)
    
    L = len(name)
    d = control(name[0])
    name[0] = "A"
    queue = deque([(name, d, 0)])
    while queue:
        _name, d, idx = queue.popleft()
        
        if _name == ['A']*L:
            answer = d
            while queue and queue[0][0] == ['A']*L:
                answer = min(answer, queue.pop()[1])
            return answer
        
        left = -1
        while _name[(idx+left)%L] == 'A':
            left -= 1

        left_name, next = _name[:], (idx+left)%L
        _d = d - left + control(_name[next])
        left_name[next] = 'A'
        queue.append((left_name, _d, next))
        print('left', left_name, _d, next)
        
        right = 1
        while _name[(idx+right)%L] == 'A':
            right += 1
        
        right_name, next = _name[:], (idx+right)%L
        _d = d + right + control(_name[next])
        right_name[next] = 'A'
        queue.append((right_name, _d, next))
        print('right', right_name, _d, next)
        print()

from collections import deque

print('정답', solution("BBBAAAAAAAB"))

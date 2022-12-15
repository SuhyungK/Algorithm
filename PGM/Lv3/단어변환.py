def check(a, b):
    cnt = 0
    for char in a:
        if char not in b:
            cnt += 1
            if cnt > 1:
                return False
            continue
        b = b.replace(char, ' ', 1)
    return cnt == 1

def solution(begin, target, words):
    # BFS
    
    queue = deque([begin])
    visited = defaultdict(int)
    while queue:
        w = queue.popleft()
            
        for word in words:
            if visited[word] or not check(w, word):
                continue
                
            visited[word] = visited[w]+1
            if word == target:
                break
                
            queue.append(word)
        
    return visited[target]

from collections import deque, defaultdict
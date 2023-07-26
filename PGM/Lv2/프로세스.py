def solution(priorities, location):
    answer = 0
    queue = deque([(idx, x) for idx, x in enumerate(priorities)])

    while queue:
        i, x = queue.popleft()

        for j, y in queue:
            if x < y:
                queue.append((i, x))
                break
        else:
            answer += 1
            if i == location:
                return answer

from collections import deque
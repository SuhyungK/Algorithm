def solution(n, k, enemy):
    
    if len(enemy) <= k:
        return len(enemy)
    
    defense = []
    heapq.heapify(defense)
    for round, attack in enumerate(enemy):
        heapq.heappush(defense, attack)
        if round >= k:
            n -= heapq.heappop(defense)
            if n < 0:
                return round
    return len(enemy)
    
import heapq
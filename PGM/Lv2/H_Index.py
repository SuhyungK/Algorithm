def solution(citations):
    L = len(citations)
    citations.sort()
    
    citations.insert(0, -1)
    
    for h in range(L+1):
        print(h)
        if citations[L-h] <= h:
            return h
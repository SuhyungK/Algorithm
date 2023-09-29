def solution(m, n, startX, startY, balls):
    answer = []
    
    for bx, by in balls:
        dis = [1e9] * 4
        
        if startX != bx or startY < by: # ↓
            dis[0] = (startY+by)**2 + (startX-bx)**2
        if startY != by or startX > bx: # →
            dis[1] = (m-startX+m-bx)**2 + (startY-by)**2
        if startX != bx or startY > by: # ↑
            dis[2] = (startX-bx)**2 + (n-startY+n-by)**2
        if startY != by or startX < bx: # ←
            dis[3] = (startX+bx)** 2 + (startY-by)**2
        
        print(dis)
        answer.append(min(dis))
    return answer
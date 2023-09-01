"""
1. 애초에 P 주변이 전부다 X면 확인할 필요가 없음
2. 근데 만약에 P 주변(상하좌우)에 P가 하나라도 있다면 바로 return 0
3. P는 없지만 O가 하나라도 있다면 O 주변의 상하좌우 확인
4. 5x5라서 중복으로 확인해도 시간초과는 안 날듯? 
"""

def solution(places):
    answer = []
    
    def distance(place, _x, _y):
        # 상하좌우 먼저 확인
        # 전부다 X면 통과 True 반환
        # P가 하나라도 있으면 False 반환
        # O가 하나라도 있으면 그 상하좌우도 확인 P 있으면 바로 False
        queue = [(_x, _y, 'P')]
        while queue:
            x, y, s = queue.pop(0)
            for nx, ny in (x-1, y), (x+1, y), (x, y+1), (x, y-1):
                if nx<0 or ny<0 or nx>=5 or ny>=5:
                    continue
                if s == 'O' and (nx, ny) == (_x, _y):
                    continue
                if place[nx][ny] == 'P':
                    return False
                if s == 'P' and place[nx][ny] == 'O':
                    queue.append((nx, ny, 'O'))
                    
        return True
    
    # 각 place의 각각의 P에 대해 확인
    def each_place(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not distance(place, i, j):
                    return 0
        return 1
                    
    for place in places:
        answer.append(each_place(place))
    return answer
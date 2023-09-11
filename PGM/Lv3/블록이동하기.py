def solution(board): 
    # 2칸에 대해 왼쪽 위에 있는 칸을 먼저 저장
    # 방문처리를 하고 큐에 추가
    def save_key(x1, y1, x2, y2, step):
        if (x1, y1) < (x2, y2):
            key = x1, y1, x2, y2
        else:
            key = x2, y2, x1, y1
        visited[key] = step
        Q.append(key)
    
    # 방문 가능한 칸인지 확인
    def is_valid(x1, y1, x2, y2):
        # 범위를 벗어나는 경우
        if not(-1<x1<n and -1<y1<n and -1<x2<n and -1<y2<n):
            return False
        # 한쪽이 벽인 경우
        if board[x1][y1] or board[x2][y2]:
            return False
        # 이미 방문한 곳인 경우
        if (x1, y1, x2, y2) in visited or (x2, y2, x1, y1) in visited:
            return False
        return True

    n = len(board)
    Q, visited = deque(), defaultdict(int)
    Q.append((0, 0, 0, 1))
    visited[(0, 0, 0, 1)] = 1
    while Q:
        x1, y1, x2, y2 = Q.popleft()
        step = visited[(x1, y1, x2, y2)]
        if (n-1, n-1) in ((x1, y1), (x2, y2)):
            print(visited)
            return step-1
        
        step += 1
        # 가로세로 모두 상하좌우 이동 가능
        if is_valid(x1-1, y1, x2-1, y2):
            save_key(x1-1, y1, x2-1, y2, step)
        if is_valid(x1+1, y1, x2+1, y2):
            save_key(x1+1, y1, x2+1, y2, step)
        if is_valid(x1, y1-1, x2, y2-1):
            save_key(x1, y1-1, x2, y2-1, step)
        if is_valid(x1, y1+1, x2, y2+1):
            save_key(x1, y1+1, x2, y2+1, step)
        if x1 == x2: # 가로일 때 각각의 기준점에 대해 시계/반시계 회전
            if x1>0:
                if not board[x1-1][y2] and is_valid(x1-1, y1, x1, y1):
                    save_key(x1, y1, x1-1, y1, step)
                if not board[x2-1][y1] and is_valid(x2-1, y2, x2, y2):
                    save_key(x2-1, y2, x2, y2, step)
            if x1<n-1:
                if not board[x1+1][y2] and is_valid(x1, y1, x1+1, y1):
                    save_key(x1, y1, x1+1, y1, step)
                if not board[x2+1][y1] and is_valid(x2, y2, x2+1, y2):
                    save_key(x2, y2, x2+1, y2, step)
        else:
            if y1>0:
                if not board[x2][y1-1] and is_valid(x1, y1, x1, y1-1):
                    save_key(x1, y1, x1, y1-1, step)
                if not board[x1][y1-1] and is_valid(x2, y2, x2, y1-1):
                    save_key(x2, y2, x2, y1-1, step)
            if y1<n-1:
                if not board[x2][y1+1] and is_valid(x1, y1, x1, y1+1):
                    save_key(x1, y1, x1, y1+1, step)
                if not board[x1][y1+1] and is_valid(x2, y2, x2, y1+1):
                    save_key(x2, y2, x2, y1+1, step)
       
from collections import deque, defaultdict
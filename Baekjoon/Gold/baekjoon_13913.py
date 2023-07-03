# 숨바꼭질 4

from collections import deque

N, K = map(int, input().split())
path, visited = [], [-1]*100001

def bfs(start, target):
    queue = deque()
    queue.append((start, 0))

    # visited 배열에 이전의 위치를 기록
    # queue에 이동한 시간(cur_time) 기록

    # target을 발견하면 이전으로 한칸씩 이동하다가 
    # 최초 지점(visited가 start인 곳)을 만나면 종료
    visited[start] = start
    while queue:
        now, move_time = queue.popleft()

        if now == target:
            cur = now

            # visited[cur]에는 cur에 오기 직전의 위치가 기록되어 있음
            # 출발점에 도착하면 출발점은 path에 추가되지 않고 종료되므로 따로 추가해줘야 함
            while cur != start:
                path.append(cur)
                cur = visited[cur]
            path.append(start)
            return move_time
        
        if now+1 < 100001 and visited[now+1] == -1:
            visited[now+1] = now
            queue.append((now+1, move_time+1))
        
        if now-1 > -1 and visited[now-1] == -1:
            visited[now-1] = now
            queue.append((now-1, move_time+1))

        if now*2 < 100001 and visited[2*now] == -1:
            visited[2*now] = now
            queue.append((2*now, move_time+1))

print(bfs(N, K))
print(*path[::-1])
N, K = int(input()), int(input())
board = [[0] * N for _ in range(N)]
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

# 사과는 2
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

L, times = int(input()), []
for _ in range(L):
    time, dir = input().split()
    times.append((int(time), dir))

def dummy():
    dir, now = 0, 1
    snake = [(0, 0)]
    while True:
        r, c = snake[-1]
        
        # 일단 몸 늘리기
        nr, nc = r+dr[dir], c+dc[dir]

        # 뱀이 벽에 부딪히거나 자기 자신을 만나게 되면 게임 종료
        if (nr<0 or nr>=N or nc<0 or nc>=N) or (nr, nc) in snake:
            return now
        
        # 이동은 무조건 하기 때문에 머리는 반드시 이동
        snake.append((nr, nc))

        # 사과가 있는 자리였다면 머리가 차지
        if board[nr][nc]:
            board[nr][nc] = 0
        
        # 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸 비워줌
        else:
            snake.pop(0)

        # 한 과정이 끝난 후 방향이 바뀔 가능성이 있나 확인
        if times and now == (change:=times[0])[0]:
            if change[1] == 'D':
                dir = (dir+1)%4
            else:
                dir = (dir+3)%4
            times.pop(0)

        # 모든 과정이 종료됐으니 1초 증가
        now += 1

print(dummy())
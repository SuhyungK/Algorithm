# 컨베이어 벨트 위의 로봇

N, K = map(int, input().split())
drblt = list(map(int, input().split()))
robot = [False] * 2*N

def find_step():
    step = cnt_zero = 0
    down, t = N-1, 2*N
    while cnt_zero < K:
        # 1. 컨베이어 벨트의 이동(로봇과 함께 이동)
        down = (down+t-1) % t
        up = down-N+1
        robot[down] = False

        # 2. 벨트 이동 방향에 따라 로봇 이동
        for i in range(down-1, up-1, -1):
            if robot[i] and not robot[i+1] and drblt[i+1]:
                robot[i+1] = True
                robot[i] = False
                drblt[i+1] -= 1
                if drblt[i+1] == 0:
                    cnt_zero += 1
        robot[down] = False

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
        if drblt[up]:
            drblt[up] -= 1
            if drblt[up] == 0:
                cnt_zero += 1
            robot[up] = True
        
        step += 1

    return step

print(find_step())
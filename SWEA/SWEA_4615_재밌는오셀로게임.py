import sys
sys.stdin = open('4615.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[-1] * n for _ in range(n)]
    board[n//2][n//2] = board[n//2 - 1][n//2 - 1] = 2
    board[n//2 - 1][n//2] = board[n//2][n//2 - 1] = 1

    cnt = [2, 2]
    dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    for _ in range(m):
        i, j, ot = map(int, input().split())
        board[i - 1][j - 1] = ot
        cnt[ot - 1] += 1
        for dx, dy in dxy:
            nx = (i - 1) + dx
            ny = (j - 1) + dy
            # 현재 돌을 놓은 지점에서 8방향으로 살펴서
            # 흑일 땐 백, 백일 땐 흑인 지점을 찾아서 그쪽 방향으로 벽의 끝까지(n) 탐색
            if 0 <= nx < n and 0 <= ny < n and abs(ot - board[nx][ny]) == 1:
                cntV = 1
                for _ in range(n):
                    nx += dx
                    ny += dy
                    if 0 <= nx < n and 0 <= ny < n:
                        # 다른 돌이면 계속 진행 : 1 2 2 2 1 인 경우
                        if abs(ot - board[nx][ny]) == 1:
                            cntV += 1
                        # 같은 돌이면 종료하고 카운트 더해주기
                        elif board[nx][ny] == ot:
                            cnt[ot - 1] += cntV
                            cnt[ot - 2] -= cntV
                            dx *= (-1)
                            dy *= (-1)
                            # 현재 돌까지 돌아오면서 돌 색깔 변경
                            while 0 <= nx + dx < n and 0 <= ny + dy < n and board[nx + dx][ny + dy] != ot:
                                nx += dx
                                ny += dy
                                board[nx][ny] = ot
                            break
                        else: break
                    else: break
    print(f'#{tc}', *cnt)
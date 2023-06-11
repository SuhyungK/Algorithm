# 재밌는 오셀로 게임

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]

    mid = n // 2
    board[mid][mid] = board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = board[mid][mid - 1] = 1

    cnt = [2, 2]

    for _ in range(m):
        i, j, ot = map(int, input().split())
        board[i - 1][j - 1] = ot
        cnt[ot - 1] += 1
        for dx, dy in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
            nx, ny = (i-1) + dx, (j-1) + dy
            while 1:
                cntV = 0
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 0: # 0일 경우 진행할 이유X
                        break
                    elif board[nx][ny] != ot: # 같지 않은 경우 계속 진행
                        nx += dx
                        ny += dy
                    elif board[nx][ny] == ot: # 같은 경우 종료하고 되돌아오면서 돌 색깔 변경 + 카운트 동시에
                                              # 1 1 인 경우 while 문에서 걸러지기 때문에 바로 break
                        dx *= (-1)
                        dy *= (-1)
                        while 0 <= nx + dx < n and 0 <= ny + dy < n and board[nx + dx][ny + dy] != ot:
                            nx += dx
                            ny += dy
                            # 1인 경우 1인 칸에 +, 2인 칸에 -
                            # 2인 경우 2인 칸에 +, 1인 칸에 -
                            cnt[ot - 1] += 1
                            cnt[ot - 2] -= 1
                            board[nx][ny] = ot
                        break
                else: break
    print(f'#{tc}', *cnt)
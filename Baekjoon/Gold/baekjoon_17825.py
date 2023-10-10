# 주사위 윷놀이 

""" 
* board
    - [다음으로 이동할 칸의 번호, 현재 칸에서 획득할 수 있는 점수]
"""
board = [[0, 0] for _ in range(33)]
for i in range(20):
    board[i] = [i+1, i*2]
board[21], board[22], board[23] = [22, 13], [23, 16], [29, 19]
board[24], board[25] = [25, 22], [29, 24]
board[26], board[27], board[28] = [27, 28], [28, 27], [29, 26]
board[29], board[30], board[31] = [30, 25], [31, 30], [20, 35]
board[20], board[32] = [32, 40], [0, 0]

DICE = list(map(int, input().split()))
horse = [0]*4 # 말의 현재 위치
"""
* 전체 경우의 수 모두 구하기
    - i : 주사위 번호
    - j : 말의 번호
"""
def dfs(i, score):
    global ans 

    if score + 40*(10-i) <= ans:
        return 
    
    if i == 10:
        if ans < score:
            ans = max(ans, score)
        return
    
    for j in range(4):
        start = next = horse[j]
        if start == 32: # 이미 도착한 경우 제외
            continue
        x = DICE[i]

        while x:
            if x == DICE[i]:
                if start == 5:
                    next = 21
                elif start == 10:
                    next = 24
                elif start == 15:
                    next = 26
                else:
                    next = board[next][0]
            else:
                next = board[next][0]
            if next == 32:
                x = 0
                continue
            x -= 1

        if next != 32 and next in horse: # 도착지가 아닌데 다른 말이 도착지점에 이미 있음
            continue

        horse[j] = next
        dfs(i+1, score+board[next][1])
        horse[j] = start

ans = 0
dfs(0, 0)
print(ans)
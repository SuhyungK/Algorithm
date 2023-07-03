# 파이프 옮기기 1

import sys
sys.setrecursionlimit(10000)

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# 대각선 확인
def checkDiag(x, y):
    return not house[x][y+1] and not house[x+1][y] and not house[x+1][y+1]

# 세로 확인
def checkVer(x, y):
    return not house[x+1][y]

# 가로 확인
def checkHori(x, y):
    return not house[x][y+1]

ans = 0
# direct : 어떤 방향으로 놓여있는지
def pushPipe(x, y, direct):
    global ans

    if (x, y) == (N-1, N-1):
        ans += 1
        return 
    
    # 가로인 경우
    if direct == 0:
        # 가로 방향 확인
        if y<N-1:
            if checkHori(x, y):
                pushPipe(x, y+1, 0)
        
        # 대각선 방향 확인
        if x<N-1 and y<N-1:
            if checkDiag(x, y):
                pushPipe(x+1, y+1, 2)
    
    # 세로인 경우
    elif direct == 1:
        if x<N-1:
            if checkVer(x, y):
                pushPipe(x+1, y, 1)
        
        if x<N-1 and y<N-1:
            if checkDiag(x, y):
                pushPipe(x+1, y+1, 2)
    
    elif direct == 2:
        if y<N-1:
            if checkHori(x, y):
                pushPipe(x, y+1, 0)

        if x<N-1:
            if checkVer(x, y):
                pushPipe(x+1, y, 1)

        if x<N-1 and y<N-1:
            if checkDiag(x, y):
                pushPipe(x+1, y+1, 2)
        
pushPipe(0, 1, 0)
print(ans)
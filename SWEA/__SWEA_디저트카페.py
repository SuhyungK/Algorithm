import sys
sys.stdin = open('test.txt', 'r')

"""
현재 위치에서 4방향으로 디저트 가게를 조사하게 되는데

"""
def dfs(r, c, idx, cnt):
    if idx == 4:
        return
    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    maxV = -1
    for i in range(N-2):
        for j in range(1, N-1):
            cnt = 0
            dessert = {}
            maxV = max(maxV, dfs(i, j, 0))
                
    print(f'#{tc}')
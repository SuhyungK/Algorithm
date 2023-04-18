import sys
sys.stdin = open('input.txt')

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _  in range(N)]

t = min(N, M) // 2

for i in range(t):
    endX, endY = N - (i+1), M - (i+1)
    cur = (endX + endY) * 2
    r = cur // R
    x = y = i
    for _ in range(cur * r):
        print()
        for row in arr:
            print(row)
        print(y, x, endX)
        if y == 0 and 0 <= x < endX:
            arr[x][y], arr[x+1][y] = arr[x+1][y], arr[x][y]
            x += 1
        elif 0 <= y < endY and x == endX:
            arr[x][y+1], arr[x][y] = arr[x][y], arr[x][y+1]
            y += 1
        elif y == endY and 0 < x <= endX:
            arr[x][y], arr[x-1][y] = arr[x-1][y], arr[x][y]
            x -= 1
        elif x == 0 and 0 < y <= endY:
            arr[x][y], arr[x][y-1] = arr[x][y], arr[x][y-1]
            y -= 1
    
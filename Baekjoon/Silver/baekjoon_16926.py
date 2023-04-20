# 배열 돌리기 1

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _  in range(N)]

t = min(N, M) // 2

endY, endX = N, M
for i in range(t):
    endX -= 1
    endY -= 1
    bord = (endX + endY - 2*i) * 2
    r = R % bord
    x = y = i
    for _ in range((bord-1) * r):
        if y == i and i <= x < endX:
            arr[y][x], arr[y][x+1] = arr[y][x+1], arr[y][x]
            x += 1
        elif i <= y < endY and x == endX:
            arr[y][x], arr[y+1][x] = arr[y+1][x], arr[y][x]
            y += 1
        elif y == endY and i < x <= endX:
            arr[y][x], arr[y][x-1] = arr[y][x-1], arr[y][x]
            x -= 1
        elif x == i and i < y <= endY:
            arr[y][x], arr[y-1][x] = arr[y-1][x], arr[y][x]
            y -= 1
    
for row in arr:
    print(*row)
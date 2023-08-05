def solution(n):
    dx = (1, 0, -1)
    dy = (0, 1, -1)
    arr = [[0] * n for _ in range(n)]

    def draw_triangle(n):
        num, d, x, y = 1, 0, -1, 0
        while True:
            if n == 0:
                break

            for _ in range(n):
                x += dx[d]
                y += dy[d]
                arr[x][y] = num
                num += 1

            n -= 1
            d = (d+1)%3

    draw_triangle(n)

    answer = []
    for i in range(n):
        answer.extend(arr[i][:i+1])

    return answer
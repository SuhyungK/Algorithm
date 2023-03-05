# S1 Z

N, r, c = map(int, input().split())

x = y = 2 ** (N-1)
ans = 0
while N > 0:
    step = 2 ** (N-2)
    cnt = 4 ** (N-1)

    if r < y and c < x:
        x -= step
        y -= step
    elif r < y and c >= x:
        y -= step
        x += step
        ans += cnt
    elif r >= y and c < x:  
        x -= step
        y += step
        ans += cnt * 2
    elif r >= y and c >= x:
        x += step
        y += step
        ans += cnt * 3
    N -= 1

print(ans)
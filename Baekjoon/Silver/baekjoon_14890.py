# 경사로

def fore():
    pass

def back():
    pass

N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for row in MAP:
    t, next = row[0], 1
    while next < N:
        if t == row[next]:
            continue

        gap = t-row[next]
        if gap > 1:
            break
        if gap == -1:
            fore()
        elif gap == 1:
            back()
    else:
        ans += 1
# 경사로

def fore(row, s, n): # 행, 시작점 값
    for t in range(1, L+1):
        if s+t>N: return N

        if row[s+t] == n and not ramp[s+t]:
            pass
    return True


def back():
    pass

N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for row in MAP:
    t, next = row[0], 1
    ramp = [False]*N
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
        
        if next >= N:
            break
    else:
        ans += 1
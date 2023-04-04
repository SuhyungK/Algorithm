# 마인크래프트

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

land = {}
for i in range(N):
    for j in range(M):
        if land.get(arr[i][j]):
            land[arr[i][j]] += 1
        else:
            land[arr[i][j]] = 1

mindC = (1e9, 1e9)
maxH = max(land.keys())
for h in range(maxH + 1):
    bct = B
    t = 0
    for k, v in land.items():
        tmp = (h - k) * v
        bct -= tmp
        if tmp > 0:
            t += tmp
        else:
            t -= tmp * 2
    if bct >= 0:
        mindC = min(mindC, (t, (-1) * h))

print(mindC[0], mindC[1] * (-1))
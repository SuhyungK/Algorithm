# 여행 가자

N, M = int(input()), int(input())
city = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x) -1, input().split()))
uni = [0] * N

i = 0
while 1:
    i += 1
    if 0 not in uni:
        break
    u = uni.index(0)
    uni[u], q = i, [u]
    while q:
        s = q.pop(0)
        for idx, e in enumerate(city[s]):
            if e and not uni[idx]:
                uni[idx] = i
                q.append(idx)

for j in range(M-1):
    s, e = plan[j], plan[j+1]
    if uni[s] != uni[e]:
        print('NO')
        break
else:
    print('YES')
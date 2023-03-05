# G5 호석이 두 마리 치킨

N, M = map(int, input().split())
bldn = [[] for _ in range(N)]
dis = [[0] * N for _ in range(N)]

for _ in range(M):
    i, j = map(lambda x: int(x) -1, input().split())
    bldn[i].append(j)
    bldn[j].append(i)

for i in range(N):
    q = [i]
    d = 0
    while q:
        s = q.pop(0)
        d += 1
        for e in bldn[s]:
            if not dis[i][e]:
                q.append(e)
                dis[i][e] = d
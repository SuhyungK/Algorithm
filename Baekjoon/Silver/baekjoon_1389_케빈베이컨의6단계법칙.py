def dfs(n):
    global cnt
    for i in range(1, N):
        q = [n]
        visit = [0] * (N + 1)
        while q:
            if q == n:
                cnt = 0
                break
            for j in frns[i]:
                if visit[j] == 0:
                    visit[j] = 1
                    q.append(j)

    return cnt

N, M = map(int, input().split()) 
users = [list(map(int, input().split())) for _ in range(M)]
frns = [[] for _ in range(N + 1)] 

for user in users:
    a, b = user
    frns[a].append(b)
    frns[b].append(a)

minV = (1e9, 1e9)
for n in range(1, N+1):
    cnt = 0
    minV = min(minV, (n, dfs(n)))

print(minV)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

cnt = 0
for i in range(1, N + 1):
    if visit[i] == 0:
        visit[i] = 1
        stack = [i]
        cnt += 1
        while stack:
            s = stack.pop()
            for w in node[s]:
                if visit[w] == 0:
                    stack.append(w)
                    visit[w] = 1

print(cnt)
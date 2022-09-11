N = int(input())
virus = [[] for _ in range(N+1)]
visit = [0] * (N+1)
visit[1] = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    virus[a].append(b)
    virus[b].append(a)

def bfs():
    queue = [1]
    cnt = 0
    while queue:
        st = queue.pop(0)
        for s in virus[st]:
            if not visit[s]:
                visit[s] = 1
                cnt += 1
                queue.append(s)

    return cnt

print(bfs())
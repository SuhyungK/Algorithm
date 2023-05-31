# 스타트링크

def bfs():
    queue = [(S, 0)]
    while queue:
        s, c = queue.pop(0)
        if s == G:
            return c
        
        for next in s+U, s-D:
            if next<1 or next>F or visit[next]:
                continue
            visit[next] = 1
            queue.append((next, c+1))

    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
visit = [0]*(F+1)

print(bfs()) 
# 특정 거리의 도시 찾기

import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().strip().split())
    arr[a].append(b)

def bfs():
    visited = [0] * (N+1)
    Q, dist = [X], 0
    visited[X] = 1
    while Q:
        
        new_Q = []
        for x in Q:
            for y in arr[x]:
                if visited[y]:
                    continue

                visited[y] = 1
                new_Q.append(y)
        
        dist += 1
        if dist == K:
            break
        Q = new_Q[:]

    new_Q.sort()
    if len(new_Q):
        print('\n'.join(map(str, new_Q)))
        return
    print(-1)
    
bfs()
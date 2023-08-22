# 끝나지 않는 파티

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
res = []
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    if graph[a-1][b-1] <= c:
        res.append("Enjoy other party")
    else:
        print("Stay here")
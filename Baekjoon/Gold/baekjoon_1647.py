# 도시 분할 계획
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    par_a = find(a)
    par_b = find(b)

    if par_a < par_b:
        parent[par_b] = par_a
    else:
        parent[par_a] = par_b

n, m = map(int, input().split())
graph = []
parent = [i for i in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a-1, b-1, c))

graph.sort(key=lambda x: x[-1])
cost = 0
count = 0
for a, b, c in graph:
    if count == n-2:
        break

    if find(a) != find(b):
        union(a, b)
        cost += c
        count += 1

print(cost)
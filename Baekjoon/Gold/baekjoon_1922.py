# 네트워크 연결

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N = int(input())
M = int(input())
route = [list(map(int, input().split())) for _ in range(M)]
parent = [i for i in range(N+1)]

cost = 0
route.sort(key=lambda x: x[-1])
for a, b, c in route:
    if find(a) == find(b):
        continue
    union(a, b)
    cost += c

print(cost)
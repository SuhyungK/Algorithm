# 별자리 만들기

def calc_dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = parent[x]
    y = parent[y]

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
lines = [list(map(lambda x: int(float(x) * 100), input().split())) for _ in range(n)]
parent = [i for i in range(n)]

distance = []
for i in range(n):
    for j in range(n):
        distance.append((i, j, calc_dist(*lines[i], *lines[j])))

distance.sort(key=lambda x: x[2])
count = 0
for a, b, d in distance:
    if find(a) != find(b):
        union(a, b)
        count += d

print(int(count)*0.01)
# 행성 터널

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

def find_dist(lst, k):
    global dist
    for i in range(N-1):
        x, y = lst[i][0], lst[i+1][0]
        if x < y:
            dist.append((x, y, abs(lst[i][1][k]-lst[i+1][1][k])))
        else:
            dist.append((y, x, abs(lst[i][1][k]-lst[i+1][1][k])))

N = int(input())
planet = [[i, list(map(int, input().split()))] for i in range(N)]
parent = [x for x in range(N)]
dist = []

for i in range(3):
    print(sorted(planet, key=lambda x: x[1][i]))
    find_dist(sorted(planet, key=lambda x: x[1][i]), i)

dist.sort(key=lambda x: x[-1])
cost = 0
for x, y, d in dist:
    if find(x) == find(y):
        continue
    union(x, y)
    cost += d

print(cost)
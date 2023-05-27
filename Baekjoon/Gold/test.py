def find(x):
    if rep[x] != x:
        return find(rep[x])
    return rep[x]

def union(x, y):
    rep[find(y)] = find(x) 

def cycle():
    pass


N, M = map(int, input().split())
rep = [n for n in range(N)]

for m in range(M):
    i, j = map(int, input().split())
    union(i, j)
    print(m, rep)
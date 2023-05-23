
def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]

def union(a, b):
    if (a:=find(a)) < (b:=find(b)):
        rep[b] = a
    else:
        rep[a] = b

def sol():
    start = rep[plan[0]]
    for j in range(1, M):
        if rep[plan[j]] != start:
            return 'NO'
    return 'YES'

N, M = int(input()), int(input())
rep = [n for n in range(N)]
link = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x)-1, input().split()))

for i in range(N):
    for j in range(N):
        if link[i][j]:
            union(i, j)

print(sol())
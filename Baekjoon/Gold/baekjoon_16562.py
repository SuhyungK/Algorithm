# 친구비

def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if A[x] <= A[y]:
        rep[y] = x 
    else:
        rep[x] = y

N, M, K = map(int, input().split())
A = [0]+list(map(int, input().split()))
rep = [i for i in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    if find(v) == find(w):
        continue
    union(v, w)

rep_lst = list(set(find(i) for i in range(1, N+1)))
cost = 0
for x in rep_lst:
    cost += A[x]
    if cost > K:
        print("Oh no")
        exit()
print(cost)
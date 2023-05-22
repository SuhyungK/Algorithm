# 게리맨더링

def bfs(lst):
    queue = [lst[0]]
    v = [lst[0]]
    while queue:
        s = queue.pop(0)
        for t in regions[s]:
            if t in lst and t not in v: 
                v.append(t)
                queue.append(t)
    
    v = sorted(list(set(v)))
    lst.sort()
    return v == lst

def make_B(arr):
    tmp = []
    for i in range(1, N+1):
        if i not in arr:
            tmp.append(i)

    return tmp
    
def main():
    diff = 1e9
    for i in range(1, 2**N):
        dist =[]
        for j in range(N):
            if i & (1<<j):
                dist.append(j+1)
        if len(dist) == N:
            continue
        if bfs(dist) and bfs(make_B(dist)):
            A = sum([pols[d] for d in dist])
            diff = min(diff, abs(2*A-total))
    
    if diff == 1e9:
        return -1
    return diff
    
N = int(input())
pols = [0] + list(map(int, input().split()))
total = sum(pols)

regions = [[]]
for _ in range(N):
    lst = list(map(int, input().split()))
    regions.append(lst[1:])

print(main())

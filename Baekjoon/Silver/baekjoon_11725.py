# 트리의 부모 찾기

from collections import defaultdict

def sol():
    stack = [1]
    while stack:
        p = stack.pop()

        for c in grpah[p]:
            if parent[c] != -1:
                continue
            parent[c] = p
            stack.append(c)

grpah = defaultdict(list)
n = int(input())
for _ in range(n-1):
    a, b = map(int, input().split())
    grpah[a].append(b)
    grpah[b].append(a)

parent = [-1]*(n+1)
parent[1] = 1
sol()

for j in range(2, n+1):
    print(parent[j])
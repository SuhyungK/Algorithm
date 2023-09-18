# 소문난 칠공주

from itertools import combinations

def find_SY(arr):
    S, Y = [], []
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'S':
                S.append(i*5+j)
            elif arr[i][j] == 'Y':
                Y.append(i*5+j)
    return S, Y

def dfs(n, comb, route):
    if n not in comb or n in route:
        return route
    
    route.add(n)
    if len(route) == 7:
        return route
    
    x, y = divmod(n, 5)
    if x > 0:
        route = dfs(n-5, comb, route)
    if x < 4:
        route = dfs(n+5, comb, route)
    if y > 0:
        route = dfs(n-1, comb, route)
    if y < 4:
        route = dfs(n+1, comb, route)
    return route

arr = [input() for _ in range(5)]
S, Y = find_SY(arr)

combs = set()
for k in range(4, 8):
    if len(S) < k:
        break
    for s_combs in combinations(S, k):
        for y_combs in combinations(Y, 7-k):
            combs.add(s_combs+y_combs)

ans = 0
for comb in combs:
    if {*comb} == dfs(comb[0], {*comb}, set()):
        ans += 1

print(ans)
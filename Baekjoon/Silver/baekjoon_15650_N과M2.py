def dfs(s):
    if len(lst) == m:
        print(*lst)

    for i in range(s, n+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()

n, m = map(int, input().split())
lst = []

dfs(1)
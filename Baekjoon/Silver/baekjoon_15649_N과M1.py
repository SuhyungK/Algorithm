def backTracking():
    if len(lst) == M:
        print(*lst)
    else:
        for i in range(1, N+1):
            if i not in lst:
                lst.append(i)
                backTracking()
                lst.pop()

N, M = map(int, input().split())
lst = []
backTracking()
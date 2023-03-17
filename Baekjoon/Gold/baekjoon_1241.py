N = int(input())
lst = [int(input()) for _ in range(N)]

matrix = {}
for l in lst:
    if matrix.get(l): matrix[l] += 1
    else: matrix[l] = 1

ans = [0 for _ in range(N)]
for i in range(N):
    for k in range(1, (l:=lst[i])**0.5 + 1):
        if not l % k:
            if matrix.get(k): ans[l] += matrix[k]
            if k * k != l and matrix.get(l//k): ans[l] += matrix[l//k]

print(ans)
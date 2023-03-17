N = int(input())
lst = [int(input()) for _ in range(N)]

matrix = {}
for l in lst:
    if matrix.get(l): matrix[l] += 1
    else: matrix[l] = 1

ans = [-1 for _ in range(N)]
for i in range(N):
    l = lst[i]
    for k in range(1, int(l**0.5) + 1):
        if not l % k:
            if matrix.get(k): ans[i] += matrix[k]
            if k * k != l and matrix.get(l//k): ans[i] += matrix[l//k]

print(ans)
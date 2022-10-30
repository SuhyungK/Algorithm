K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

lo, hi = 1, max(lan)
while lo <= hi:
    mid = (lo + hi) // 2
    n = sum([l//mid for l in lan])

    if n >= N:
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)